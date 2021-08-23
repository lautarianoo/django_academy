from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Category, Course
from django.views import View

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
        course= Course.objects.get(id=kwargs.get('pk'))
        return render(request, 'courses/course_detail.html', {'course': course})

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
            Q(certificate=request.GET.get('cert')) |
            Q(status_money=request.GET.get('free'))
        ).distinct()
        return render(request, 'base.html', {'courses': courses})
