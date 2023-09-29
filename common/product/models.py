from django.db import models
from django.utils import timezone

from common.users.base import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"

    def __str__(self):
        return self.title


class File(BaseModel):
    file = models.FileField(verbose_name="Файл", upload_to='uploadFiles')

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
        return f"ID # {self.title}"


class ProductStatus(models.IntegerChoices):
    HasDiscount = 1, "Имеет скидку"
    NoDiscount = 2, "Нет скидки"


class Product(BaseModel):
    category = models.ForeignKey(Category, verbose_name="Категория продукта", related_name='categoryProducts',
                                 on_delete=models.SET_NULL, null=True, blank=True)
    code = models.CharField(max_length=50, verbose_name="Код", null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="Название")
    photo = models.ImageField("Image of Product", upload_to='productImage', null=True, blank=True)
    # photo_medium = ImageSpecField(source='photo', processors=[ResizeToFill(800, 600)], format='PNG',
    #                               options={'quality': 100})
    # photo_small = ImageSpecField(source='photo', processors=[ResizeToFill(400, 300)], format='PNG',
    #                              options={'quality': 100})
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
        return self.title
