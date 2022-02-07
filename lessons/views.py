from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import ContentUnit, SectionTopic, TopicCourse
from courses.models import Course

class ContentCourseView(View):

    def get(self, request, *args, **kwargs):
        if 'unit' not in request.GET.keys():
            return redirect('profile')
        topics = TopicCourse.objects.all()
        section = SectionTopic.objects.get(id=kwargs.get('section_id'))
        unit = ContentUnit.objects.filter(section=section, step_id=request.GET.get('unit')).first()
        return render(request, 'lessons/content_course.html', {'section': section, 'unit': unit, 'topics': topics, 'topic': topics[0],
                                                               'next_step_id': unit.step_id + 1})

#class CheckAnswerTestView(View):
#
#    def get(self, request, *args, **kwargs):
#        test = Test.objects.get(id=kwargs.get('id'))
#        for variant, status in request.GET.items():
#            if variant == test.right_answer:
#                request.user.complete_tests.add(test)
#                request.user.balls += 1
#                messages.add_message(request, messages.SUCCESS, 'Ответ правильный. Задание выполнено')
#                return redirect('test_edu', pk=test.section.topic.course.id, id=test.section.id, test=test.id)
#        messages.add_message(request, messages.ERROR, 'Ответ неправильный')
#        return redirect('test_edu', pk=test.section.topic.course.id, id=test.section.id, test=test.id)
