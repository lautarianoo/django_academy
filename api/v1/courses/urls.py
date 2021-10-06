from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListAPI.as_view()),
    path('category/<int:pk>/', views.CategoryDetailAPI.as_view()),
    path('courses/', views.CourseListAPI.as_view()),
    path('course/<int:pk>/', views.CourseDetailAPI.as_view())
]
