# Generated by Django 3.2.9 on 2022-02-05 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariantTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(max_length=60, verbose_name='Вариант')),
            ],
        ),
        migrations.CreateModel(
            name='TopicCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тема курса')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='courses.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Тема курса',
                'verbose_name_plural': 'Темы курса',
            },
        ),
        migrations.CreateModel(
            name='SectionTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('balls', models.IntegerField(default=1, verbose_name='Количество баллов за урок')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='lessons.topiccourse', verbose_name='Тема курса')),
            ],
            options={
                'verbose_name': 'Cекция',
                'verbose_name_plural': 'Секции',
            },
        ),
        migrations.CreateModel(
            name='ContentUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название урока')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Контент урока')),
                ('test', models.BooleanField(default=False)),
                ('multiple_choice', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('right_variants', models.ManyToManyField(blank=True, null=True, related_name='right_variant_unit', to='lessons.VariantTest', verbose_name='Правильный вариант')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='units', to='lessons.sectiontopic', verbose_name='Секция уроков')),
                ('variants', models.ManyToManyField(blank=True, null=True, related_name='variant_unit', to='lessons.VariantTest', verbose_name='Варианты ответа')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
