from rest_framework import serializers
from courses.models import Category, Course

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', 'slug', )

class CourseSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    class Meta:
        model = Course
        fields = ('title', 'category',
                  'short_description', 'description', 'members',
                  'community', 'requirements', 'author',
                  'language', 'status_money', 'price', 'status_certificate', 'travel_time')
