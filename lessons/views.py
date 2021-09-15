from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Lesson, Test, SectionTopic, TopicCourse
from courses.models import Course
from .forms import RightAnswerTestForm

class TopicsCourseView(View):

    def get(self, request, *args, **kwargs):
        topics = TopicCourse.objects.filter(course_id=kwargs.get('pk'))
        section = SectionTopic.objects.filter(topic=topics.first()).first()
        lesson = Lesson.objects.filter(section=section).first()
        return render(request, 'lessons/lessons_course.html', {'topics': topics, 'lesson': lesson})

class SectionView(View):

    def get(self, request, *args, **kwargs):
        topics = TopicCourse.objects.filter(course_id=kwargs.get('pk'))
        section = SectionTopic.objects.get(id=kwargs.get('id'))
        lesson_first = Lesson.objects.filter(section=section).first()
        return render(request, 'lessons/section.html', {'section': section, 'lesson_first': lesson_first, 'topics': topics})

class LessonView(View):

    def get(self, request, *args, **kwargs):
        topics = TopicCourse.objects.filter(course=kwargs.get('pk'))
        section = SectionTopic.objects.get(id=kwargs.get('id'))
        lesson = Lesson.objects.get(id=kwargs.get('lesson'))
        return render(request, 'lessons/section_lessons.html', {'section': section, 'lesson': lesson, 'topics': topics})

class TestView(View):

    def get(self, request, *args, **kwargs):
        topics = TopicCourse.objects.filter(course=kwargs.get('pk'))
        section = SectionTopic.objects.get(id=kwargs.get('id'))
        test = Test.objects.get(id=kwargs.get('test'))
        variants = {'variant_1': test.variant_1, 'variant_2': test.variant_2,
                    'variant_3': test.variant_3}
        if test.variant_4:
            variants['variant_4'] = test.variant_4
        if test.variant_5:
            variants['variant_5'] = test.variant_5
        if test.variant_6:
            variants['variant_6'] = test.variant_6
        if test.variant_7:
            variants['variant_7'] = test.variant_7
        return render(request, 'lessons/section_tests.html', {'section': section, 'test': test, 'variants': variants, 'topics': topics})

class CheckAnswerTestView(View):

    def get(self, request, *args, **kwargs):
        test = Test.objects.get(id=kwargs.get('id'))
        for variant, status in request.GET.items():
            if variant == test.right_answer:
                request.user.complete_tests.add(test)
                messages.add_message(request, messages.SUCCESS, 'Ответ правильный. Задание выполнено')
                return redirect('test_edu', pk=test.section.topic.course.id, id=test.section.id, test=test.id)
        messages.add_message(request, messages.ERROR, 'Ответ неправильный')
        return redirect('test_edu', pk=test.section.topic.course.id, id=test.section.id, test=test.id)
