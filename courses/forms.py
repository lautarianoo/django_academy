from django import forms
from .models import Feedback

class FeedbackAddForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = (
            'text', 'mark',
        )
