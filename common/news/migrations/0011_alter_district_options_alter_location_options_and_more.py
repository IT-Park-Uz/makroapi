# Generated by Django 4.2.3 on 2023-09-23 07:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0010_alter_location_close_alter_location_open_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="district",
            options={"verbose_name": "Pайоны", "verbose_name_plural": "Pайоны"},
        ),
        migrations.AlterModelOptions(
            name="location",
            options={"verbose_name": "Расположение", "verbose_name_plural": "Расположение"},
        ),
        migrations.AlterModelOptions(
            name="news",
            options={"ordering": ["startDate"], "verbose_name": "Новости", "verbose_name_plural": "Новости"},
        ),
        migrations.AlterModelOptions(
            name="region",
            options={"verbose_name": "Pегионы", "verbose_name_plural": "Pегионы"},
        ),
        migrations.AlterField(
            model_name="district",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="regionDistrict",
                to="news.region",
                verbose_name="Pегион",
            ),
        ),
        migrations.AlterField(
            model_name="district",
            name="title",
            field=models.CharField(max_length=150, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="location",
            name="address",
            field=models.CharField(max_length=300, verbose_name="Pайон"),
        ),
        migrations.AlterField(
            model_name="location",
            name="close",
            field=models.TimeField(default=django.utils.timezone.now, verbose_name="Закрывать"),
        ),
        migrations.AlterField(
            model_name="location",
            name="district",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="districtLocation",
                to="news.district",
                verbose_name="Pайон",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="open",
            field=models.TimeField(default=django.utils.timezone.now, verbose_name="Открыть"),
        ),
        migrations.AlterField(
            model_name="news",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="news",
            name="endDate",
            field=models.DateField(default=django.utils.timezone.now, verbose_name="Время окончания"),
        ),
        migrations.AlterField(
            model_name="news",
            name="startDate",
            field=models.DateField(default=django.utils.timezone.now, verbose_name="Время начала"),
        ),
        migrations.AlterField(
            model_name="news",
            name="status",
            field=models.IntegerField(choices=[(1, "АКТИВНЫЙ"), (2, "АРХИВ")], default=1, verbose_name="Статус"),
        ),
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="news",
            name="videoURL",
            field=models.URLField(blank=True, null=True, verbose_name="URL-адрес видео"),
        ),
        migrations.AlterField(
            model_name="region",
            name="title",
            field=models.CharField(max_length=150, verbose_name="Название"),
        ),
    ]
