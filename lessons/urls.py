from django.urls import path
from .views import *

urlpatterns = [
    path('<int:course_id>/step/<int:section_id>', ContentCourseView.as_view(), name='content_view'),
    path('<int:test_id>', CheckAnswerTestView.as_view(), name='check_answer'),
    path('edit-create/<int:pk>/topic-create', CreateTopic.as_view(), name='topic-create')
]
