import os
from datetime import datetime

from django.conf import settings
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db import models
from django.utils import timezone

from common.users.base import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"

    def __str__(self):
        return f"Категория: {self.title}"


class TopCategory(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Название")

    class Meta:
        verbose_name = "Высшая категория"
        verbose_name_plural = "Высшая категория"

    def __str__(self):
        return f"Высшая категория: {self.title}"


class File(BaseModel):
    file = models.FileField(verbose_name="Файл", upload_to='uploadFiles')
    images_file = models.FileField(verbose_name="Архив с изображениями", upload_to='upload_image_files')
    processed = models.IntegerField(verbose_name="Обработано", default=0)
    total = models.IntegerField(verbose_name="Всего продуктов", default=0)
    message = models.TextField()

    class Meta:
        ordering = ['-id']
        verbose_name = "Файл"
        verbose_name_plural = "Файл"

    def __str__(self):
        return f"ID # {self.id}"


class CatalogFile(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Название")
    file = models.FileField(verbose_name="Файл", upload_to='uploadFiles')
    endDate = models.DateField(default=timezone.now, verbose_name="Время окончания")

    class Meta:
        ordering = ['-id']
        verbose_name = "Оферты"
        verbose_name_plural = "Оферты"

    def __str__(self):
        return f"Оферты # {self.title}"


class ProductStatus(models.IntegerChoices):
    HasDiscount = 1, "Имеет скидку"
    NoDiscount = 2, "Нет скидки"


def upload_to(instance, filename):
    today = datetime.now()
    return f'product_images/{today.year}/{today.month:02d}/{today.day:02d}/{filename}'


class ProductRegion(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)

    class Meta:
        verbose_name = "Регион продукта"
        verbose_name_plural = "Регионы продуктов"

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ForeignKey(Category, verbose_name="Категория продукта", related_name='categoryProducts',
                                 on_delete=models.SET_NULL, null=True, blank=True)
    top_category = models.ForeignKey(TopCategory, verbose_name="Высшая категория", related_name='Top_categoryProducts',
                                     on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(ProductRegion, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")
    code = models.CharField(max_length=50, verbose_name="Код", null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="Название")
    photo = models.ImageField("Image of Product", upload_to=upload_to, null=True, blank=True)
    newPrice = models.FloatField(default=0, verbose_name="Новая цена")
    oldPrice = models.FloatField(default=0, verbose_name="Старая цена")
    percent = models.IntegerField(default=0, verbose_name="Процент")
    startDate = models.DateField(default=timezone.now, verbose_name="Время начала")
    endDate = models.DateField(default=timezone.now, verbose_name="Время окончания")
    status = models.IntegerField(choices=ProductStatus.choices, default=ProductStatus.HasDiscount,
                                 verbose_name="Статус")

    class Meta:
        ordering = ['-id']
        verbose_name = "Продукт"
        verbose_name_plural = "Продукт"

    def __str__(self):
        return f"Продукт: {self.title}"

    def save(self, *args, **kwargs):
        if settings.STAGE == 'prod':
            if self.photo == "":  # Assuming you check if the photo is null
                self.status = ProductStatus.NoDiscount  # Set the status you want when photo is null
        super().save(*args, **kwargs)


@receiver(pre_delete, sender=Product)
def delete_product_photo(sender, instance, **kwargs):
    # Delete the photo file from the operating system when a Product object is deleted
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


# Connect the signal
pre_delete.connect(delete_product_photo, sender=Product)
