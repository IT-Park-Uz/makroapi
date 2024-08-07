# Generated by Django 4.2.5 on 2024-05-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discount", "0014_alter_discount_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="discount",
            name="photo_mobile",
            field=models.ImageField(
                default="discountImage/сайт_морожка.jpg",
                upload_to="discountImageMobile",
                verbose_name="Изображение для мобилки",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="discount",
            name="photo",
            field=models.ImageField(upload_to="discountImage", verbose_name="Изображение"),
        ),
    ]
