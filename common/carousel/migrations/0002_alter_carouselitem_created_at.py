# Generated by Django 4.2.5 on 2024-01-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carousel", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carouselitem",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
