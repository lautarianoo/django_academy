from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', TopicsCourseView.as_view(), name='edu_course'),
    path('<int:pk>/<int:id>/', SectionView.as_view(), name='section_edu'),
    path('<int:pk>/<int:id>/lesson/<int:lesson>/', LessonView.as_view(), name='lesson_edu'),
    path('<int:pk>/<int:id>/test/<int:test>/', TestView.as_view(), name='test_edu'),
    path('<int:id>/checkanswer/', CheckAnswerTestView.as_view(), name='checkanswer'),
    path('teach/course/<int:pk>/settings/', CreatingLessonsTest.as_view(), name='setting_lesson_test')
]
