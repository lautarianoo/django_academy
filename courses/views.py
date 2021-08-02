from django.shortcuts import render
from .models import Category, Course
from django.views import View

class BaseView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        courses = Course.objects.all()
        return render(request, 'base.html', {'categories': categories, 'courses': courses})
