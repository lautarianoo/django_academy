from django import forms
from .models import UserAcademy

class LoginForm(forms.Form):

    email = forms.CharField(label='Почта', widget=forms.EmailInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

    def clean(self, *args, **kwargs):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not UserAcademy.objects.filter(email=email).exists():
            raise forms.ValidationError('Такого пользователя не существует')
        user = UserAcademy.objects.filter(email=email).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data

class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

    class Meta:
        model = UserAcademy
        fields = ('email', 'phone', 'first_name', 'last_name', 'avatar')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']

class SettingsForm(forms.ModelForm):

    class Meta:
        model = UserAcademy
        fields = ('phone', 'first_name', 'last_name', 'avatar')

class EmailAcceptForm(forms.Form):

    code = forms.CharField(label='Код')
