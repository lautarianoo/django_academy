from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from courses.models import Course

User = get_user_model()

class Pay(models.Model):
    '''Модель сделанных заказов'''

    account = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    item = models.ForeignKey(Course, verbose_name='Купленный курс', on_delete=models.CASCADE)
    status = models.BooleanField('Статус платежа', default=False)
    date_create = models.DateTimeField('Дата создания', default=timezone.now)
    date_complete = models.DateTimeField('Дата оплаты', blank=True, null=True)

    def __str__(self):
        return f"{self.item.title} | User: {self.account.id}"

    class Meta:
        verbose_name = 'Заказ',
        verbose_name_plural='Заказы'
