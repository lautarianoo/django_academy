from django.shortcuts import render
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
