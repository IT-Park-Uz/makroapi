# Generated by Django 4.2.5 on 2024-09-11 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0018_discount_photo_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='hide',
            field=models.BooleanField(default=False, verbose_name='Скрыть?'),
        ),
    ]