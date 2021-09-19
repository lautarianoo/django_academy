from django import forms
from .models import Feedback, Course

class FeedbackAddForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = (
            'text', 'mark',
        )

class CourseAddForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = (
            'title', 'category', 'short_description', 'description', 'community',
            'requirements', 'language', 'image', 'status_certificate'
        )

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        if Course.objects.filter(title=data['title']):
            raise forms.ValidationError('Такое название уже существует')
        return self.cleaned_data
