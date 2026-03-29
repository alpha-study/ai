from django.urls import path
from .views import (
    UploadDocumentView, AskView, HistoryView, ReprocessDocumentView,
    ChatSessionListView,
    ResearchView, ResearchHistoryView,
    GenerateMockExamView, MockExamListView, MockExamDetailView,
)

urlpatterns = [
    # Document management
    path('upload-document/',            UploadDocumentView.as_view(),       name='upload-document'),
    path('admin/reprocess/<uuid:doc_id>/', ReprocessDocumentView,           name='admin-reprocess'),

    # Chat
    path('ask/',                         AskView.as_view(),                  name='ask'),
    path('chat/sessions/',               ChatSessionListView.as_view(),      name='chat-sessions'),
    path('history/<uuid:session_id>/',   HistoryView.as_view(),              name='history'),

    # Research / Thesis assistant
    path('research/',                    ResearchView.as_view(),             name='research'),
    path('research/history/',            ResearchHistoryView.as_view(),      name='research-history'),

    # Mock Exam
    path('mock-exam/generate/',          GenerateMockExamView.as_view(),     name='mock-exam-generate'),
    path('mock-exam/',                   MockExamListView.as_view(),         name='mock-exam-list'),
    path('mock-exam/<uuid:exam_id>/',    MockExamDetailView.as_view(),       name='mock-exam-detail'),
]
