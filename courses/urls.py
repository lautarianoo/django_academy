from django.urls import path
from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('add-member/<int:pk>/', AddMemberCourse.as_view(), name='add_member'),
    path('add-course/', AddCourseView.as_view(), name='add_course'),
    path('search', SearchCourse.as_view(), name='search'),
    path('<int:pk>/accept-delete/', DeleteCourseAcceptView.as_view(), name='accept_delete'),
    path('<int:pk>/delete/', DeleteCourseView.as_view(), name='delete_course'),
    path('<slug:slug>/', CategoryView.as_view(), name='category'),
]
