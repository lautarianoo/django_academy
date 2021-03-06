# Generated by Django 3.2.9 on 2022-02-05 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Статус платежа')),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('date_complete', models.DateTimeField(blank=True, null=True, verbose_name='Дата оплаты')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Купленный курс')),
            ],
            options={
                'verbose_name': ('Заказ',),
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
