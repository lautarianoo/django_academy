from django.urls import path
from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('add-member/<int:pk>/', AddMemberCourse.as_view(), name='add_member'),
    path('search', SearchCourse.as_view(), name='search'),
    path('<slug:slug>/', CategoryView.as_view(), name='category'),
]
