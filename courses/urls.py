from django.urls import path
from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('<slug:slug>/', CategoryView.as_view(), name='category')
]
