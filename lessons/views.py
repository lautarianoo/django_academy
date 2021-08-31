from django.shortcuts import render
from django.views import View
from .models import Lesson, Test, SectionTopic, TopicCourse

class LessonsCourseView(View):

    def get(self, request, *args, **kwargs):
        topics = TopicCourse.objects.filter(course_id=kwargs.get('pk'))
        sections = SectionTopic.objects.filter(topic=topics.first())
        lesson = Lesson.objects.filter(section=sections.first()).first()
        return render(request, 'lessons/lessons_course.html', {'section': sections, 'topics': topics, 'lesson': lesson})

