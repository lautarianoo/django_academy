# Generated by Django 3.2.9 on 2022-02-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_contentunit_step_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentunit',
            name='right_variants',
            field=models.ManyToManyField(blank=True, related_name='right_variant_unit', to='lessons.VariantTest', verbose_name='Правильный вариант'),
        ),
        migrations.AlterField(
            model_name='contentunit',
            name='variants',
            field=models.ManyToManyField(blank=True, related_name='variant_unit', to='lessons.VariantTest', verbose_name='Варианты ответа'),
        ),
    ]