# Generated by Django 4.2.5 on 2023-11-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0017_newscatalog"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newscatalog",
            name="photo",
        ),
        migrations.AddField(
            model_name="newscatalog",
            name="photo_ru",
            field=models.ImageField(
                blank=True, null=True, upload_to="newsCatalogImage", verbose_name="Изображение ru"
            ),
        ),
        migrations.AddField(
            model_name="newscatalog",
            name="photo_uz",
            field=models.ImageField(
                blank=True, null=True, upload_to="newsCatalogImage", verbose_name="Изображение uz"
            ),
        ),
    ]