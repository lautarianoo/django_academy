from django.db import models
from courses.models import Course

class TopicCourse(models.Model):

    title = models.CharField(max_length=100, verbose_name='Тема курса')
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'

class SectionTopic(models.Model):

    title = models.CharField(max_length=100, verbose_name='Секция темы')
    topic = models.ForeignKey(TopicCourse, verbose_name='Тема курса', on_delete=models.CASCADE)
    balls = models.IntegerField(default=1, verbose_name='Количество баллов за урок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

class LessonAbstract(models.Model):

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        abstract = True

    title = models.CharField(max_length=100, verbose_name='Название урока')
    section = models.ForeignKey(SectionTopic, verbose_name='Секция уроков', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} | {self.section.title}'

