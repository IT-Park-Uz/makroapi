# Generated by Django 4.2.3 on 2023-09-23 07:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("discount", "0007_alter_discount_enddate_alter_discount_startdate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="endDate",
            field=models.DateField(default=django.utils.timezone.now, verbose_name="Время окончания"),
        ),
        migrations.AlterField(
            model_name="discount",
            name="startDate",
            field=models.DateField(default=django.utils.timezone.now, verbose_name="Время начала"),
        ),
        migrations.AlterField(
            model_name="discount",
            name="status",
            field=models.IntegerField(choices=[(1, "АКТИВНЫЙ"), (2, "АРХИВ")], default=1, verbose_name="Статус"),
        ),
    ]
