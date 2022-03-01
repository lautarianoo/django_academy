from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import ContentUnit, SectionTopic, TopicCourse, VariantTest
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

class CheckAnswerTestView(View):

    def get(self, request, *args, **kwargs):
        test = ContentUnit.objects.filter(id=kwargs.get('test_id')).first()
        true_list = []
        r_variants = [variant.variant for variant in test.right_variants.all()]
        if len(request.GET.getlist('select')) == len(test.right_variants.all()) or not test.multiple_choice:
            if test.multiple_choice:
                for select_variant_id in request.GET.getlist('select'):
                    variant = VariantTest.objects.filter(id=int(select_variant_id)).first()
                    if variant.variant in r_variants:
                        true_list.append(True)
                    else:
                        true_list.append(False)
            else:
                select_variant_id = request.GET.get('select_variant')
                print(select_variant_id)
                variant = VariantTest.objects.filter(id=int(select_variant_id)).first()
                if variant.variant in r_variants:
                    true_list.append(True)
                else:
                    true_list.append(False)
            if all(true_list):
                request.user.complete_tests.add(test)
                response = redirect('content_view', course_id=test.section.topic.course.id, section_id=test.section.id)
                response['Location'] += '?unit=' + str(test.id)
                return response
        messages.add_message(request, messages.ERROR, 'Ответ неправильный')
        response = redirect('content_view', course_id=test.section.topic.course.id, section_id=test.section.id)
        response['Location'] += '?unit=' + str(test.id)
        return response

class CreateTopic(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'lessons/create_topic.html', {})

    def post(self, request, *args, **kwargs):
        new_topic = TopicCourse.objects.create(title=request.POST.get('name', course=Course.objects.get(id=kwargs.get('course_id'))))
        new_topic.save()
        return redirect('create_and_edit', pk=kwargs.get('course_id'))