# Generated by Django 4.2.5 on 2024-06-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0022_remove_news_photo_medium_mobile"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="views_count",
            field=models.IntegerField(default=0),
        ),
    ]
