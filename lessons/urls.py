from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', TopicsCourseView.as_view(), name='edu_course'),
    path('<int:pk>/<int:id>/', SectionView.as_view(), name='section_edu'),
    path('<int:pk>/<int:id>/lesson/<int:lesson>/', LessonView.as_view(), name='lesson_edu'),
    path('<int:pk>/<int:id>/test/<int:test>/', TestView.as_view(), name='test_edu'),
    path('<int:id>/checkanswer/', CheckAnswerTestView.as_view(), name='checkanswer'),
    path('teach/course/<int:pk>/settings/', CreatingLessonsTest.as_view(), name='setting_lesson_test'),
    path('teach/course/<int:pk>/create/topic/', TopicCreate.as_view(), name='topic_create'),
    path('teach/course/<int:pk>/create/section/', SectionCreate.as_view(), name='section_create'),
    path('teach/course/<int:pk>/create/lesson/', LessonCreate.as_view(), name='lesson_create'),
    path('teach/course/<int:pk>/create/test/', TestCreate.as_view(), name='test_create'),
]
