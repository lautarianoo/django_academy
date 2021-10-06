from rest_framework import generics, permissions

from courses.models import Category, Course
from .serializers import CourseSerializer, CategorySerializer

class CategoryListAPI(generics.ListAPIView):

    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Category.objects.all()

class CategoryDetailAPI(generics.RetrieveAPIView):

    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Course.objects.filter(category_id=self.kwargs.get('pk'))

class CourseListAPI(generics.ListAPIView):

    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Course.objects.all()

class CourseDetailAPI(generics.RetrieveAPIView):

    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Course.objects.filter(id=self.kwargs.get('pk'))
