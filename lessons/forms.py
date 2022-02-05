from django import forms
from .models import TopicCourse, SectionTopic

class TopicCreateForm(forms.ModelForm):

    class Meta:
        model = TopicCourse
        fields = ('title', 'course', )


class SectionCreateForm(forms.ModelForm):
    class Meta:
        model = SectionTopic
        fields = ('title', 'topic',)

