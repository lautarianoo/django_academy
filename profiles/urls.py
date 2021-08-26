from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/', ProfileUserView.as_view(), name='profile_user'),
    path('settings/', SettingsView.as_view(), name='settings')
]
