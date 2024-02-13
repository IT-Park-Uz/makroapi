# Generated by Django 4.2.5 on 2024-02-13 13:55

from django.db import migrations, models
import django.db.models.deletion


def create_objects(apps, schema_editor):
    ProductRegion = apps.get_model('product', 'ProductRegion')
    Product = apps.get_model('product', 'Product')
    # Create objects here
    ProductRegion.objects.create(id=1, name_ru="Ташкент", name_uz="Toshkent")
    ProductRegion.objects.create(id=2, name_ru="Ферганская долина", name_uz="Farg'ona vodiysi")
    Product.objects.all().update(region_id=1)


def reverse_objects(apps, schema_editor):
    ...


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0018_alter_product_photo"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductRegion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("name_uz", models.CharField(max_length=100, null=True, verbose_name="Название")),
                ("name_ru", models.CharField(max_length=100, null=True, verbose_name="Название")),
            ],
            options={
                "verbose_name": "Регион продукта",
                "verbose_name_plural": "Регионы продуктов",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="region",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="product.productregion",
            ),
        ),
        migrations.RunPython(create_objects, reverse_objects),
    ]
