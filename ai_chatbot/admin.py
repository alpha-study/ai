from django.contrib import admin
from .models import ChatSession, ChatMessage, KnowledgeDocument, DocumentChunk, ResearchQuery, MockExam, MockExamQuestion


@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'role', 'created_at')


@admin.register(KnowledgeDocument)
class KnowledgeDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploaded_by', 'uploaded_at', 'processed')
    actions = ['reprocess']

    def reprocess(self, request, queryset):
        from .tasks import process_document
        for doc in queryset:
            process_document.delay(str(doc.id))


@admin.register(DocumentChunk)
class DocumentChunkAdmin(admin.ModelAdmin):
    list_display = ('id', 'document', 'created_at')


@admin.register(ResearchQuery)
class ResearchQueryAdmin(admin.ModelAdmin):
    list_display  = ('id', 'user', 'topic', 'tokens_used', 'created_at')
    list_filter   = ('created_at',)
    search_fields = ('topic', 'query')
    readonly_fields = ('id', 'user', 'topic', 'query', 'response', 'sources', 'tokens_used', 'created_at')


class MockExamQuestionInline(admin.TabularInline):
    model  = MockExamQuestion
    extra  = 0
    fields = ('question_number', 'question_type', 'question_text', 'correct_answer', 'marks')
    readonly_fields = fields


@admin.register(MockExam)
class MockExamAdmin(admin.ModelAdmin):
    list_display  = ('id', 'user', 'subject', 'topic', 'difficulty', 'question_type', 'num_questions', 'created_at')
    list_filter   = ('difficulty', 'question_type', 'created_at')
    search_fields = ('subject', 'topic')
    readonly_fields = ('id', 'user', 'tokens_used', 'created_at')
    inlines       = [MockExamQuestionInline]


@admin.register(MockExamQuestion)
class MockExamQuestionAdmin(admin.ModelAdmin):
    list_display  = ('question_number', 'exam', 'question_type', 'marks')
    list_filter   = ('question_type',)
    search_fields = ('question_text',)
