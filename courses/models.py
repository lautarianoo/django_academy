from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Category(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    school_predmet = models.BooleanField(default=False, verbose_name='Предмет')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Course(models.Model):

    LANGUAGE = (
        ('Русский', 'Русский'),
        ('Английский', 'Английский'),
        ('Немецкий', 'Немецкий'),
        ('Французский', 'Французкий'),
        ('Испанский', 'Испанский'),
    )

    STATUS_FORMONEY = (
        ('Платный', 'Платный'),
        ('Бесплатный', 'Бесплатный'),
    )

    CERTIFICATE = (
        ('Выдаётся', 'Выдаётся'),
        ('Не выдаётся', 'Не выдаётся')
    )

    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    members = models.ManyToManyField(User, verbose_name='Участники курса', related_name='courses')
    short_description = models.TextField(max_length=1200)
    description = models.TextField(max_length=3500)
    community = models.TextField(max_length=900, verbose_name='На кого расчитан курс')
    requirements  = models.TextField(max_length=900, verbose_name='Требования')
    author = models.ForeignKey(User, verbose_name='Автор курса', on_delete=models.CASCADE)
    language = models.CharField(choices=LANGUAGE, max_length=200, verbose_name='Язык', null=True)
    image = models.ImageField()
    status_money = models.BooleanField(default=False, verbose_name='Платный')
    #TODO: ХУЙНЮ СНИЗУ УДАЛИТЬ
    status_formoney = models.CharField(max_length=50, verbose_name='Платный или бесплатный', choices=STATUS_FORMONEY)
    price = models.IntegerField(default=0, verbose_name='Цена курса', blank=True, null=True)
    status_certificate = models.BooleanField(default=False, verbose_name='Сертификат', null=True)
    certificate = models.CharField(max_length=50, verbose_name='Сертификат', choices=CERTIFICATE)
    travel_time = models.PositiveIntegerField(default=1, verbose_name='Примерное время прохождения')
    date_add = models.DateField(auto_now_add=True)

    def get_members_count(self):
        return self.members.count()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
