# Generated by Django 4.2.5 on 2023-09-08 17:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="status",
            field=models.IntegerField(choices=[(1, "HasDiscount"), (2, "NoDiscount")], default=1),
        ),
    ]
