from rest_framework import serializers
from .models import KnowledgeDocument, MockExam, MockExamQuestion, ResearchQuery, ChatSession, ChatMessage


class UploadDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeDocument
        fields = ('id', 'title', 'file', 'file_type')

    def validate_file(self, value):
        max_size = 50 * 1024 * 1024
        if value.size > max_size:
            raise serializers.ValidationError('File too large (max 50MB).')
        return value

    def validate(self, attrs):
        f = attrs.get('file')
        file_type = attrs.get('file_type')
        if f and file_type:
            name = f.name.lower()
            if file_type == 'pdf' and not name.endswith('.pdf'):
                raise serializers.ValidationError('file_type does not match file extension')
            if file_type == 'txt' and not name.endswith('.txt'):
                raise serializers.ValidationError('file_type does not match file extension')
            if file_type == 'json' and not name.endswith('.json'):
                raise serializers.ValidationError('file_type does not match file extension')
            if file_type == 'docx' and not name.endswith('.docx'):
                raise serializers.ValidationError('file_type does not match file extension')
        return attrs


class AskSerializer(serializers.Serializer):
    session_id = serializers.UUIDField(required=True)
    question   = serializers.CharField()


# ── Chat History ─────────────────────────────────────────────────────────────

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ChatMessage
        fields = ('id', 'role', 'message', 'response', 'tokens_used', 'created_at')
        read_only_fields = fields


class ChatSessionSerializer(serializers.ModelSerializer):
    """Lightweight session list item with last message preview."""
    message_count = serializers.SerializerMethodField()
    last_message  = serializers.SerializerMethodField()

    class Meta:
        model  = ChatSession
        fields = ('id', 'created_at', 'updated_at', 'message_count', 'last_message')
        read_only_fields = fields

    def get_message_count(self, obj):
        # Only count assistant turns (one per Q-A pair)
        return obj.messages.filter(role='assistant').count()

    def get_last_message(self, obj):
        last = obj.messages.filter(role='user').order_by('-created_at').first()
        if last:
            text = last.message
            return text[:120] + '…' if len(text) > 120 else text
        return None


# ── Research / Thesis ────────────────────────────────────────────────────────

class ResearchQuerySerializer(serializers.Serializer):
    """Request body for the research assistant endpoint."""
    topic         = serializers.CharField(max_length=512, required=False, default='')
    query         = serializers.CharField()
    research_type = serializers.ChoiceField(
        choices=['overview', 'thesis', 'literature', 'methodology',
                 'analysis', 'conclusion', 'bibliography'],
        default='overview',
        required=False,
    )


class ResearchQueryDetailSerializer(serializers.ModelSerializer):
    """Response body for a saved research query."""
    class Meta:
        model   = ResearchQuery
        fields  = ('id', 'topic', 'query', 'response', 'sources',
                   'tokens_used', 'created_at')
        read_only_fields = fields


# ── Mock Exam ─────────────────────────────────────────────────────────────────

class MockExamRequestSerializer(serializers.Serializer):
    """Request body for generating a mock exam."""
    subject       = serializers.CharField(max_length=256)
    topic         = serializers.CharField(max_length=512)
    difficulty    = serializers.ChoiceField(
        choices=['easy', 'medium', 'hard', 'mixed'],
        default='medium', required=False,
    )
    question_type = serializers.ChoiceField(
        choices=['mcq', 'short_answer', 'true_false', 'mixed'],
        default='mcq', required=False,
    )
    num_questions     = serializers.IntegerField(min_value=1, max_value=30, default=10, required=False)
    time_limit_minutes = serializers.IntegerField(min_value=1, required=False, allow_null=True, default=None)


class MockExamQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MockExamQuestion
        fields = ('id', 'question_number', 'question_type', 'question_text',
                  'options', 'correct_answer', 'explanation', 'marks')
        read_only_fields = fields


class MockExamDetailSerializer(serializers.ModelSerializer):
    questions = MockExamQuestionSerializer(many=True, read_only=True)

    class Meta:
        model  = MockExam
        fields = ('id', 'subject', 'topic', 'difficulty', 'question_type',
                  'num_questions', 'time_limit_minutes', 'instructions',
                  'tokens_used', 'created_at', 'questions')
        read_only_fields = fields


class MockExamListSerializer(serializers.ModelSerializer):
    """Lightweight list view — no questions payload."""
    question_count = serializers.IntegerField(source='questions.count', read_only=True)

    class Meta:
        model  = MockExam
        fields = ('id', 'subject', 'topic', 'difficulty', 'question_type',
                  'num_questions', 'time_limit_minutes', 'created_at', 'question_count')
        read_only_fields = fields
