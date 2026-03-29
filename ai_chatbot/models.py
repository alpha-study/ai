import uuid
from django.db import models
from django.conf import settings


class ChatSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChatMessage(models.Model):
    ROLE_CHOICES = (('user', 'user'), ('assistant', 'assistant'))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE)
    role = models.CharField(max_length=16, choices=ROLE_CHOICES)
    message = models.TextField()
    response = models.TextField(null=True, blank=True)
    tokens_used = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class KnowledgeDocument(models.Model):
    FILE_TYPES = (('pdf', 'pdf'), ('txt', 'txt'), ('json', 'json'), ('docx', 'docx'))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=512)
    file = models.FileField(upload_to='knowledge_docs/')
    file_type = models.CharField(max_length=16, choices=FILE_TYPES)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    metadata = models.JSONField(default=dict, blank=True)


class DocumentChunk(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document = models.ForeignKey(KnowledgeDocument, related_name='chunks', on_delete=models.CASCADE)
    chunk_text = models.TextField()
    embedding_vector = models.BinaryField(null=True, blank=True)
    vector_id = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ResearchQuery(models.Model):
    """Stores student research / thesis assistance queries and AI responses."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    topic = models.CharField(max_length=512)
    query = models.TextField()
    response = models.TextField(blank=True, default='')
    sources = models.JSONField(default=list, blank=True)
    tokens_used = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"ResearchQuery({self.topic!r}) by {self.user}"


class MockExam(models.Model):
    """Header record for a generated mock exam."""
    DIFFICULTY_CHOICES = (
        ('easy',   'Easy'),
        ('medium', 'Medium'),
        ('hard',   'Hard'),
        ('mixed',  'Mixed'),
    )
    QUESTION_TYPE_CHOICES = (
        ('mcq',           'Multiple Choice (MCQ)'),
        ('short_answer',  'Short Answer'),
        ('true_false',    'True / False'),
        ('mixed',         'Mixed'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=256)
    topic = models.CharField(max_length=512)
    difficulty = models.CharField(max_length=16, choices=DIFFICULTY_CHOICES, default='medium')
    question_type = models.CharField(max_length=16, choices=QUESTION_TYPE_CHOICES, default='mcq')
    num_questions = models.PositiveIntegerField(default=10)
    time_limit_minutes = models.PositiveIntegerField(null=True, blank=True)
    instructions = models.TextField(blank=True, default='')
    tokens_used = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"MockExam({self.subject} – {self.topic}, {self.difficulty})"


class MockExamQuestion(models.Model):
    """Individual question belonging to a MockExam."""
    QUESTION_TYPE_CHOICES = (
        ('mcq',           'Multiple Choice (MCQ)'),
        ('short_answer',  'Short Answer'),
        ('true_false',    'True / False'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exam = models.ForeignKey(MockExam, related_name='questions', on_delete=models.CASCADE)
    question_number = models.PositiveIntegerField()
    question_type = models.CharField(max_length=16, choices=QUESTION_TYPE_CHOICES, default='mcq')
    question_text = models.TextField()
    # For MCQ: stored as a JSON list of 4 strings e.g. ["A. ...", "B. ...", ...]
    options = models.JSONField(default=list, blank=True)
    correct_answer = models.TextField()
    explanation = models.TextField(blank=True, default='')
    marks = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['question_number']

    def __str__(self):
        return f"Q{self.question_number} ({self.question_type}) – {self.exam}"
