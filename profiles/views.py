from django.contrib.auth import logout, authenticate, login, get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import LoginForm, RegisterForm, SettingsForm, EmailAcceptForm
from courses.models import Course
from utils.send_mail import generate_code, send_email

User = get_user_model()

class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('base'))
        return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

class RegisterView(View):

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return HttpResponseRedirect(reverse('login'))
        return render(request, 'users/register.html', {'form': form})

class ProfileView(View):
    '''Свой профиль'''
    def get(self, request, *args, **kwargs):
        courses = Course.objects.filter(members__exact=request.user)
        return render(request, 'users/profile.html', {'courses': courses, 'user': request.user})

class ProfileUserView(View):
    '''Чужой профиль'''
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs.get('pk'))
        return render(request, 'users/profile_user.html', {'user': user})

class SettingsView(View):

    def get(self, request, *args, **kwargs):
        form = SettingsForm(initial={'phone': request.user.phone,
                                     'first_name': request.user.first_name, 'last_name': request.user.last_name,
                                     })
        return render(request, 'users/settings.html', {'form': form})

    def post(self, request, *args, **kwargs):
        user = request.user
        form = SettingsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            data = form.cleaned_data
            user.phone = data['phone']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.avatar = data['avatar']
            user.save()
            return HttpResponseRedirect(reverse('profile'))
        return render(request, 'users/settings.html', {'form': form})

class MyAuthorCourseView(View):

    def get(self, request, *args, **kwargs):
        courses = Course.objects.filter(author=request.user)
        return render(request, 'users/profile_teach.html', {'courses': courses, 'user': request.user})

class AuthorCourseView(View):

    def get(self, request, *args, **kwargs):
        courses = Course.objects.filter(author=kwargs.get('pk'))
        user = User.objects.get(id=kwargs.get('pk'))
        return render(request, 'users/profile_user_teach.html', {'courses': courses, 'user': user})

class EmailView(View):

    def get(self, request, *args, **kwargs):
        code = generate_code()
        send_email(request.user.email, code)
        return render(request, 'users/accept_email.html', {'code': code})

class AcceptEmailView(View):

    def get(self, request, *args, **kwargs):
        if not request.user.status_email:
            if request.GET['code'] == kwargs.get('code'):
                request.user.status_email = True
                request.user.save()
                return redirect('settings')
        return redirect('profile')
