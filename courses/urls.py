from django.urls import path
from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='base')
]
