# Generated by Django 4.2.3 on 2023-09-23 07:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0008_alter_product_enddate_alter_product_startdate"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категория"},
        ),
        migrations.AlterModelOptions(
            name="file",
            options={"ordering": ["-id"], "verbose_name": "Файл", "verbose_name_plural": "Файл"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ["-id"], "verbose_name": "Продукт", "verbose_name_plural": "Продукт"},
        ),
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(upload_to="uploadFiles", verbose_name="Файл"),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="categoryProducts",
                to="product.category",
                verbose_name="Категория продукта",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="code",
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Код"),
        ),
        migrations.AlterField(
            model_name="product",
            name="endDate",
            field=models.DateField(default=django.utils.timezone.now, verbose_name="Время окончания"),
        ),
        migrations.AlterField(
            model_name="product",
            name="newPrice",
            field=models.FloatField(default=0, verbose_name="Новая цена"),
        ),
        migrations.AlterField(
            model_name="product",
            name="oldPrice",
            field=models.FloatField(default=0, verbose_name="Старая цена"),
        ),
        migrations.AlterField(
            model_name="product",
            name="percent",
            field=models.FloatField(default=0, verbose_name="Процент"),
        ),
        migrations.AlterField(
            model_name="product",
            name="startDate",
            field=models.DateField(default=django.utils.timezone.now, verbose_name="Время начала"),
        ),
        migrations.AlterField(
            model_name="product",
            name="status",
            field=models.IntegerField(
                choices=[(1, "Имеет скидку"), (2, "Нет скидки")], default=1, verbose_name="Статус"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Название"),
        ),
    ]
