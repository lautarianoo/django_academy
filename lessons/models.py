from django.db import models
from courses.models import Course
from ckeditor_uploader.fields import RichTextUploadingField

class TopicCourse(models.Model):

    title = models.CharField(max_length=100, verbose_name='Тема курса')
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return f'{self.title} | {self.course.title}'

    class Meta:
        verbose_name = 'Тема курса'
        verbose_name_plural = 'Темы курса'

class SectionTopic(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название')
    topic = models.ForeignKey(TopicCourse, verbose_name='Тема курса', on_delete=models.CASCADE, related_name='sections')
    balls = models.IntegerField(default=1, verbose_name='Количество баллов за урок')

    def __str__(self):
        return f'{self.title} | {self.topic.title}'

    class Meta:
        verbose_name = 'Cекция'
        verbose_name_plural = 'Секции'

class VariantTest(models.Model):

    variant = models.CharField(verbose_name='Вариант', max_length=60)

class ContentUnit(models.Model):

    step_id = models.PositiveIntegerField(default=1, verbose_name='Номер степа')
    title = models.CharField(max_length=100, verbose_name='Название урока', blank=True, null=True)
    content = models.TextField(verbose_name='Контент урока', blank=True, null=True)
    section = models.ForeignKey(SectionTopic, verbose_name='Секция уроков', on_delete=models.CASCADE, related_name='units', blank=True, null=True)
    test = models.BooleanField(default=False)
    variants = models.ManyToManyField(VariantTest, verbose_name='Варианты ответа', related_name='variant_unit', blank=True)
    right_variants = models.ManyToManyField(VariantTest, verbose_name='Правильный вариант', related_name='right_variant_unit', blank=True)
    multiple_choice = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} | {self.section.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
