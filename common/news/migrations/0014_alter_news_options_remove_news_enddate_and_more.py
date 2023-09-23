# Generated by Django 4.2.3 on 2023-09-23 16:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0013_location_title"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={"verbose_name": "Новости", "verbose_name_plural": "Новости"},
        ),
        migrations.RemoveField(
            model_name="news",
            name="endDate",
        ),
        migrations.RemoveField(
            model_name="news",
            name="startDate",
        ),
        migrations.RemoveField(
            model_name="news",
            name="status",
        ),
        migrations.RemoveField(
            model_name="news",
            name="videoURL",
        ),
    ]
