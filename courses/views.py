from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Category, Course, Feedback
from django.views import View
from .forms import FeedbackAddForm

class BaseView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        courses = Course.objects.all()
        return render(request, 'base.html', {'categories': categories, 'courses': courses})

class CategoryView(View):

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(slug=kwargs.get('slug'))
        courses = Course.objects.filter(category=category)
        return render(request, 'courses/category.html', {'category': category, 'courses': courses})

class CourseDetailView(View):

    def get(self, request, *args, **kwargs):
        form = FeedbackAddForm()
        course= Course.objects.get(id=kwargs.get('pk'))
        feedbacks = Feedback.objects.filter(course=course)
        return render(request, 'courses/course_detail.html', {'course': course, 'feedbacks': feedbacks, 'form': form})

    def post(self, request, *args, **kwargs):
        form = FeedbackAddForm(request.POST or None)
        if form.is_valid():
            course = Course.objects.get(id=kwargs.get('pk'))
            new_feedback = form.save(commit=False)
            new_feedback.author = request.user
            new_feedback.course = course
            new_feedback.save()
            return redirect('course_detail', pk=course.id)
        return render(request, 'courses/course_detail.html', {'form': form})

class AddMemberCourse(View):

    def get(self, request, *args, **kwargs):
        course = Course.objects.get(id=kwargs.get('pk'))
        course.members.add(request.user)
        return redirect('course_detail', pk=kwargs.get('pk'))

class SearchCourse(View):

    def get(self, request, *args, **kwargs):

        courses = Course.objects.filter(
            Q(title__icontains=request.GET.get('q')) |
            Q(category__title__icontains=request.GET.get('q')) |
            Q(status_certificate=request.GET.get('cert')) |
            Q(status_money=request.GET.get('free'))
        ).distinct()
        return render(request, 'base.html', {'courses': courses})
