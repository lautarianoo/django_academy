from django import forms
from .models import Test, Lesson, TopicCourse, SectionTopic

class RightAnswerTestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ('variant_1', 'variant_2', 'variant_3', 'variant_4',
                  'variant_5', 'variant_6', 'variant_7')

class TopicCreateForm(forms.ModelForm):

    class Meta:
        model = TopicCourse
        fields = ('title', 'course', )


class SectionCreateForm(forms.ModelForm):
    class Meta:
        model = SectionTopic
        fields = ('title', 'topic',)


class LessonCreateForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('title', 'content', 'section')


class TestCreateForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('text', 'section', 'right_answer', 'variant_1', 'variant_2', 'variant_3', 'variant_4',
                  'variant_5', 'variant_6', 'variant_7')
