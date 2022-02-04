from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Lesson, Test, SectionTopic, TopicCourse
from courses.models import Course
from .forms import LessonCreateForm, TestCreateForm, TopicCreateForm, SectionCreateForm

class CheckAnswerTestView(View):

    def get(self, request, *args, **kwargs):
        test = Test.objects.get(id=kwargs.get('id'))
        for variant, status in request.GET.items():
            if variant == test.right_answer:
                request.user.complete_tests.add(test)
                request.user.balls += 1
                messages.add_message(request, messages.SUCCESS, 'Ответ правильный. Задание выполнено')
                return redirect('test_edu', pk=test.section.topic.course.id, id=test.section.id, test=test.id)
        messages.add_message(request, messages.ERROR, 'Ответ неправильный')
        return redirect('test_edu', pk=test.section.topic.course.id, id=test.section.id, test=test.id)

class CreatingLessonsTest(View):

    def get(self, request, *args, **kwargs):
        course = Course.objects.get(id=kwargs.get('pk'))
        topics = TopicCourse.objects.filter(course=course)
        return render(request, 'lessons/create_lessons_test.html', {'topics': topics, 'course': course})

class TopicCreate(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'lessons/topic_create.html', {'form': TopicCreateForm()})

    def post(self, request, *args, **kwargs):
        form = TopicCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('setting_lesson_test', pk=kwargs.get('pk'))
        return render(request, 'lessons/topic_create.html', {'form': TopicCreateForm()})


class SectionCreate(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'lessons/section_create.html', {'form': SectionCreateForm()})

    def post(self, request, *args, **kwargs):
        form = SectionCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('setting_lesson_test', pk=kwargs.get('pk'))
        return render(request, 'lessons/section_create.html', {'form': SectionCreateForm()})


class LessonCreate(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'lessons/lesson_create.html', {'form': LessonCreateForm()})

    def post(self, request, *args, **kwargs):
        form = LessonCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('setting_lesson_test', pk=kwargs.get('pk'))
        return render(request, 'lessons/lesson_create.html', {'form': LessonCreateForm()})


class TestCreate(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'lessons/test_create.html', {'form': TestCreateForm()})

    def post(self, request, *args, **kwargs):
        form = TestCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('setting_lesson_test', pk=kwargs.get('pk'))
        return render(request, 'lessons/test_create.html', {'form': TestCreateForm()})
