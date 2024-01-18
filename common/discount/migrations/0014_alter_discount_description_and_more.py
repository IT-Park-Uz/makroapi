# Generated by Django 4.2.5 on 2024-01-18 16:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("discount", "0013_alter_discount_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="discount",
            name="description_ru",
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="discount",
            name="description_uz",
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name="Описание"),
        ),
    ]
