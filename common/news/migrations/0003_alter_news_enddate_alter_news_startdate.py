# Generated by Django 4.2.5 on 2023-09-14 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_alter_news_enddate_alter_news_startdate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="endDate",
            field=models.DateField(default=datetime.date(2023, 9, 14)),
        ),
        migrations.AlterField(
            model_name="news",
            name="startDate",
            field=models.DateField(default=datetime.date(2023, 9, 14)),
        ),
    ]
