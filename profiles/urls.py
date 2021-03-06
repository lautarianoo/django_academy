from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/', ProfileUserView.as_view(), name='profile_user'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('profile/teach/', MyAuthorCourseView.as_view(), name='my_author_course'),
    path('<int:pk>/teach/', AuthorCourseView.as_view(), name='author_course'),
    path('acceptmail/', EmailView.as_view(), name='email-acc'),
    path('acceptmail/<str:code>/', AcceptEmailView.as_view(), name='acceptmail')
]
