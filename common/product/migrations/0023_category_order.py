# Generated by Django 4.2.5 on 2024-07-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0022_product_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="order",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
