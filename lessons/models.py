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

class Lesson(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название урока', blank=True, null=True)
    content = models.TextField(verbose_name='Контент урока')
    section = models.ForeignKey(SectionTopic, verbose_name='Секция уроков', on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return f'{self.title} | {self.section.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

class Test(models.Model):

    text = models.TextField(verbose_name='Содержимое теста')
    section = models.ForeignKey(SectionTopic, on_delete=models.CASCADE, verbose_name='секция', related_name='tests')
    right_answer = models.CharField(max_length=400, verbose_name='Правильный ответ')
    variant_1 = models.CharField(max_length=400, verbose_name='Вариант 1')
    variant_2 = models.CharField(max_length=400, verbose_name='Вариант 2')
    variant_3 = models.CharField(max_length=400, verbose_name='Вариант 3')
    variant_4 = models.CharField(max_length=400, verbose_name='Вариант 4', blank=True, null=True)
    variant_5 = models.CharField(max_length=400, verbose_name='Вариант 5', blank=True, null=True)
    variant_6 = models.CharField(max_length=400, verbose_name='Вариант 6', blank=True, null=True)
    variant_7 = models.CharField(max_length=400, verbose_name='Вариант 7', blank=True, null=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name='Тест'
        verbose_name_plural = 'Тесты'


