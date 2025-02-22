from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from common.users.base import BaseModel, BaseMeta
from ckeditor_uploader.fields import RichTextUploadingField


class DiscountStatus(models.IntegerChoices):
    ACTIVE = 1, "АКТИВНЫЙ"
    ARCHIVE = 2, "АРХИВ"


class Discount(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Название", null=True, blank=True)
    description = RichTextUploadingField(verbose_name="Описание", null=True, blank=True)
    photo = models.ImageField("Изображение", upload_to='discountImage')
    photo_medium = ImageSpecField(source='photo', processors=[ResizeToFill(1463, 420)], format='PNG',
                                  options={'quality': 100})
    photo_small = ImageSpecField(source='photo', processors=[ResizeToFill(1463, 420)], format='PNG',
                                 options={'quality': 100})
    photo_mobile = models.ImageField("Изображение для мобилки", upload_to='discountImageMobile')
    photo_app = models.ImageField(verbose_name="Изображение для приложения", upload_to='discountImageMobile',
                                  null=True, blank=True)
    # photo_medium_mobile = ImageSpecField(source='photo', processors=[ResizeToFill(1463, 420)],
    #                                      format='PNG', options={'quality': 100})
    photo_small_mobile = ImageSpecField(source='photo', processors=[ResizeToFill(1463, 420)],
                                        format='PNG', options={'quality': 100})
    status = models.IntegerField(choices=DiscountStatus.choices, verbose_name="Статус", default=DiscountStatus.ACTIVE)
    startDate = models.DateField(default=timezone.now, verbose_name="Время начала")
    endDate = models.DateField(default=timezone.now, verbose_name="Время окончания")

    titleFile = models.CharField(max_length=200, verbose_name="Название Файл", null=True, blank=True)
    file = models.FileField(verbose_name="Файл", upload_to='uploadFiles', null=True, blank=True)
    endDateFile = models.DateField(default=timezone.now, verbose_name="Файл Время окончания", null=True, blank=True)
    views_count = models.IntegerField(default=0)
    is_main = models.BooleanField(verbose_name="Показать на главной?", default=False)
    hide = models.BooleanField(default=False, verbose_name="Скрыть?")

    class Meta(BaseMeta):
        pass

    def __str__(self):
        return f"Скидка #{self.id}"


class DiscountFiles(models.Model):
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name="files")
    titleFile = models.CharField(max_length=200, verbose_name="Название Файл")
    file = models.FileField(verbose_name="Файл", upload_to='uploadFiles', null=True, blank=True)

    class Meta:
        verbose_name = "Прикрепляемые файлы"
        verbose_name_plural = "Прикрепляемые файлы"

    def __str__(self):
        return self.titleFile


class DiscountCatalog(BaseModel):
    discount = models.ForeignKey(Discount, related_name="discountCatalog", on_delete=models.CASCADE)
    photo_uz = models.ImageField(verbose_name="Изображение uz", upload_to='discountCatalogImage', null=True, blank=True)
    photo_ru = models.ImageField(verbose_name="Изображение ru", upload_to='discountCatalogImage', null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
