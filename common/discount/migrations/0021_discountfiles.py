# Generated by Django 4.2.5 on 2025-02-01 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('discount', '0020_remove_discount_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleFile', models.CharField(max_length=200, verbose_name='Название Файл')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploadFiles', verbose_name='Файл')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files',
                                               to='discount.discount')),
            ],
            options={
                'verbose_name': 'Прикрепляемые файлы',
                'verbose_name_plural': 'Прикрепляемые файлы',
            },
        ),
    ]
