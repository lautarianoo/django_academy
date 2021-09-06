from django.shortcuts import render
from django.views import View
from .models import Lesson, Test, SectionTopic, TopicCourse
from courses.models import Course

class TopicsCourseView(View):

    def get(self, request, *args, **kwargs):
        topics = TopicCourse.objects.filter(course_id=kwargs.get('pk'))
        section = SectionTopic.objects.filter(topic=topics.first()).first()
        lesson = Lesson.objects.filter(section=section).first()
        return render(request, 'lessons/lessons_course.html', {'topics': topics, 'lesson': lesson})

class LessonView(View):

    def get(self, request, *args, **kwargs):
        topics = TopicCourse.objects.filter(course=kwargs.get('pk'))
        section = SectionTopic.objects.get(id=kwargs.get('id'))
        lesson = Lesson.objects.get(id=kwargs.get('lesson'))
        return render(request, 'lessons/section_lessons.html', {'section': section, 'lesson': lesson})

class TestView(View):

    def get(self, request, *args, **kwargs):
        topics = TopicCourse.objects.filter(course=kwargs.get('pk'))
        section = SectionTopic.objects.get(id=kwargs.get('id'))
        test = Test.objects.get(id=kwargs.get('test'))
        variants = []
        return render(request, 'lessons/section_tests.html', {'section': section, 'test': test})
