from django.urls import path
from .views import *

urlpatterns = [
    path('<int:course_id>/step/<int:section_id>', ContentCourseView.as_view(), name='content_view'),

]
