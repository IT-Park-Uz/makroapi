# Generated by Django 4.2.5 on 2024-01-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discount", "0012_discountcatalog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="discountcatalog",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
