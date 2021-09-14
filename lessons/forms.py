from django import forms
from .models import Test

class RightAnswerTestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ('variant_1', 'variant_2', 'variant_3', 'variant_4',
                  'variant_5', 'variant_6', 'variant_7')

