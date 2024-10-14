# Generated by Django 4.2.5 on 2024-10-14 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='ferma')),
                ('name', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('role', models.CharField(max_length=255)),
                ('facts', models.CharField(max_length=500)),
            ],
        ),
    ]