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
        if len(request.GET.getlist('select')) == len(test.right_variants.all()):
            for select_variant_id in request.GET.getlist('select'):
                variant = VariantTest.objects.filter(id=select_variant_id).first()
                for right_variant in test.right_variants.all():
                    if variant.variant == right_variant.variant:
                        true_list.append(True)
                        break
                    else:
                        true_list.append(False)

