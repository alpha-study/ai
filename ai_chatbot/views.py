from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import ChatSession, ChatMessage, KnowledgeDocument, MockExam, MockExamQuestion, ResearchQuery
from .serializers import (
    UploadDocumentSerializer, AskSerializer,
    ChatSessionSerializer, ChatMessageSerializer,
    MockExamRequestSerializer, MockExamDetailSerializer, MockExamListSerializer,
    ResearchQuerySerializer, ResearchQueryDetailSerializer,
)
from .tasks import process_document
from .rag import retrieve_and_answer, research_and_answer, generate_mock_exam, CONVERSATION_HISTORY_WINDOW


class UploadDocumentView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = UploadDocumentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doc = serializer.save(uploaded_by_id=request.user.id)
        process_document.delay(str(doc.id))
        return Response({'id': doc.id, 'status': 'processing'}, status=status.HTTP_201_CREATED)


class AskView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id    = serializer.validated_data['user_id']
        session_id = serializer.validated_data['session_id']
        question   = serializer.validated_data['question']
        session, _ = ChatSession.objects.get_or_create(id=session_id, defaults={'user_id': user_id})

        # ── Build conversation history from prior turns in this session ──────
        # Fetch the last CONVERSATION_HISTORY_WINDOW assistant messages (each
        # stores both the user question and the AI response), ordered oldest→newest.
        prior = (
            ChatMessage.objects
            .filter(session=session, role='assistant')
            .exclude(response__isnull=True)
            .exclude(response='')
            .order_by('-created_at')[:CONVERSATION_HISTORY_WINDOW]
        )
        # Reverse so history is oldest-first (chronological)
        history = []
        for msg in reversed(prior):
            history.append({'role': 'user',      'content': msg.message})
            history.append({'role': 'assistant', 'content': msg.response})

        # Save the new user message, then call the RAG pipeline with history
        ChatMessage.objects.create(session=session, role='user', message=question)
        answer, sources, tokens = retrieve_and_answer(question, history=history or None)

        ChatMessage.objects.create(
            session=session, role='assistant',
            message=question, response=answer, tokens_used=tokens,
        )
        return Response({'answer': answer, 'sources': sources, 'tokens_used': tokens})


class ChatSessionListView(APIView):
    """
    GET /api/chatbot/chat/sessions/?user_id=<int>
    Returns all chat sessions for the given Node.js user_id,
    ordered by most recently updated, with message count and last message preview.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'user_id query parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        sessions = ChatSession.objects.filter(user_id=user_id).order_by('-updated_at')
        serializer = ChatSessionSerializer(sessions, many=True)
        return Response({
            'count':    sessions.count(),
            'sessions': serializer.data,
        })


class HistoryView(APIView):
    """
    GET /api/chatbot/history/<session_id>/?user_id=<int>
    Returns the full message history for a specific chat session.
    Requires user_id to scope the lookup to the correct owner.
    """
    permission_classes = [AllowAny]

    def get(self, request, session_id):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'user_id query parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        session  = get_object_or_404(ChatSession, id=session_id, user_id=user_id)
        messages = session.messages.order_by('created_at')
        serializer = ChatMessageSerializer(messages, many=True)
        return Response({
            'session_id':    str(session.id),
            'created_at':    session.created_at,
            'updated_at':    session.updated_at,
            'message_count': messages.filter(role='assistant').count(),
            'messages':      serializer.data,
        })


@api_view(['POST'])
@permission_classes([IsAdminUser])
def ReprocessDocumentView(request, doc_id):
    """Admin API to reprocess a document by id."""
    try:
        doc = KnowledgeDocument.objects.get(id=doc_id)
    except KnowledgeDocument.DoesNotExist:
        return JsonResponse({'error': 'document not found'}, status=404)
    process_document.delay(str(doc.id))
    return JsonResponse({'status': 'reprocessing enqueued', 'id': str(doc.id)})


# ───────────────────────────────────────────────────────────────────
#  RESEARCH / THESIS ASSISTANT
# ───────────────────────────────────────────────────────────────────

class ResearchView(APIView):
    """
    POST /api/chatbot/research/

    Body:
        {
          "topic":         "Climate Change",          // optional
          "query":         "What is global warming?",
          "research_type": "overview"                 // optional
        }

    research_type choices:
        overview | thesis | literature | methodology | analysis | conclusion | bibliography
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ResearchQuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        answer, sources, tokens = research_and_answer(
            query=data['query'],
            topic=data.get('topic', ''),
            research_type=data.get('research_type', 'overview'),
        )

        # Save the research query to the database
        rq = ResearchQuery.objects.create(
            user_id=data['user_id'],
            topic=data.get('topic', '') or data['query'][:80],
            query=data['query'],
            response=answer,
            sources=sources,
            tokens_used=tokens,
        )

        return Response({
            'id':          str(rq.id),
            'topic':       rq.topic,
            'answer':      answer,
            'sources':     sources,
            'tokens_used': tokens,
            'created_at':  rq.created_at,
        })


class ResearchHistoryView(APIView):
    """
    GET /api/chatbot/research/history/?user_id=<int>
    Returns the user's past research queries (most recent first).
    """
    permission_classes = [AllowAny]

    def get(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'user_id query parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        qs = ResearchQuery.objects.filter(user_id=user_id)[:50]
        serializer = ResearchQueryDetailSerializer(qs, many=True)
        return Response(serializer.data)


# ───────────────────────────────────────────────────────────────────
#  MOCK EXAM GENERATOR
# ───────────────────────────────────────────────────────────────────

class GenerateMockExamView(APIView):
    """
    POST /api/chatbot/mock-exam/generate/

    Body:
        {
          "subject":            "Physics",
          "topic":              "Newton's Laws of Motion",
          "difficulty":         "medium",         // easy | medium | hard | mixed
          "question_type":      "mcq",             // mcq | short_answer | true_false | mixed
          "num_questions":      10,
          "time_limit_minutes": 30                 // optional
        }

    Returns the full exam with all questions saved to the database.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = MockExamRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # Generate questions via AI
        questions_data, tokens = generate_mock_exam(
            subject=data['subject'],
            topic=data['topic'],
            difficulty=data.get('difficulty', 'medium'),
            question_type=data.get('question_type', 'mcq'),
            num_questions=data.get('num_questions', 10),
        )

        if not questions_data:
            return Response(
                {'error': 'Could not generate exam questions. Please try again.'},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        # Persist MockExam header
        exam = MockExam.objects.create(
            user_id=data['user_id'],
            subject=data['subject'],
            topic=data['topic'],
            difficulty=data.get('difficulty', 'medium'),
            question_type=data.get('question_type', 'mcq'),
            num_questions=len(questions_data),
            time_limit_minutes=data.get('time_limit_minutes'),
            tokens_used=tokens,
        )

        # Persist each question
        for q in questions_data:
            MockExamQuestion.objects.create(
                exam=exam,
                question_number=q['question_number'],
                question_type=q['question_type'],
                question_text=q['question_text'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation'],
                marks=q['marks'],
            )

        out = MockExamDetailSerializer(exam).data
        out['message'] = f"Mock exam created with {exam.questions.count()} questions."
        return Response(out, status=status.HTTP_201_CREATED)


class MockExamListView(APIView):
    """
    GET /api/chatbot/mock-exam/?user_id=<int>
    Returns all mock exams created by the specified user.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'user_id query parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        exams = MockExam.objects.filter(user_id=user_id)
        serializer = MockExamListSerializer(exams, many=True)
        return Response(serializer.data)


class MockExamDetailView(APIView):
    """
    GET /api/chatbot/mock-exam/<uuid:exam_id>/?user_id=<int>
    Returns a specific mock exam with all questions.
    """
    permission_classes = [AllowAny]

    def get(self, request, exam_id):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'user_id query parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        exam = get_object_or_404(MockExam, id=exam_id, user_id=user_id)
        serializer = MockExamDetailSerializer(exam)
        return Response(serializer.data)

    def delete(self, request, exam_id):
        """Allow users to delete their own exams."""
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'user_id query parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        exam = get_object_or_404(MockExam, id=exam_id, user_id=user_id)
        exam.delete()
        return Response({'message': 'Exam deleted.'}, status=status.HTTP_204_NO_CONTENT)
