# Generated by Django 4.2.3 on 2023-09-08 14:18

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Discount",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("guid", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("photo", models.ImageField(upload_to="discountImage", verbose_name="Image of Discount")),
                ("url", models.CharField(blank=True, max_length=250, null=True)),
                ("startDate", models.DateField(default=django.utils.timezone.now)),
                ("endDate", models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
    ]
