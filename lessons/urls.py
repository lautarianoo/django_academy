from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', TopicsCourseView.as_view(), name='edu_course'),
    path('<int:pk>/<int:id>/lesson/<int:lesson>/', LessonView.as_view(), name='lesson_edu'),
    path('<int:pk>/<int:id>/lesson/<int:test>/', TestView.as_view(), name='test_edu')
]
