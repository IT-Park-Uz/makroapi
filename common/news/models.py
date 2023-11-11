from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from common.users.base import BaseModel


class NewsStatus(models.IntegerChoices):
    ACTIVE = 1, "АКТИВНЫЙ"
    ARCHIVE = 2, "АРХИВ"


class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Название", null=True, blank=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    photo = models.ImageField(verbose_name="Изображение", upload_to='newsImage')
    photo_medium = models.ImageField(verbose_name="Детальное изображение", upload_to='newsImage', null=True, blank=True)

    # photo_medium = ImageSpecField(source='photo', processors=[ResizeToFill(1200, 350)], format='PNG',
    #                               options={'quality': 90})
    photo_small = ImageSpecField(source='photo', processors=[ResizeToFill(400, 400)], format='PNG',
                                 options={'quality': 90})

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f"Новости: {self.title_ru}"


class NewsCatalog(BaseModel):
    news = models.ForeignKey(News, related_name="newsCatalog", on_delete=models.CASCADE)
    photo_uz = models.ImageField(verbose_name="Изображение uz", upload_to='newsCatalogImage', null=True, blank=True)
    photo_ru = models.ImageField(verbose_name="Изображение ru", upload_to='newsCatalogImage', null=True, blank=True)

    def __str__(self):
        return f"{self.id}"


class Region(BaseModel):
    title = models.CharField(max_length=150, verbose_name="Название")

    class Meta:
        verbose_name = "Pегионы"
        verbose_name_plural = "Pегионы"

    def __str__(self):
        return f"Pегионы: {self.title}"


class District(BaseModel):
    region = models.ForeignKey(Region, verbose_name="Pегион", related_name="regionDistrict", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name="Название")

    class Meta:
        verbose_name = "Pайоны"
        verbose_name_plural = "Pайоны"

    def __str__(self):
        return f"Pайоны: {self.title}"


class Location(BaseModel):
    district = models.ForeignKey(District, verbose_name="Pайон", related_name="districtLocation",
                                 on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=150, verbose_name="Название")
    address = models.CharField(max_length=300, verbose_name="Адрес")
    longitude = models.CharField(max_length=60, null=True, blank=True)
    latitude = models.CharField(max_length=60, null=True, blank=True)
    open = models.TimeField(default=timezone.now, verbose_name="Открыть")
    close = models.TimeField(default=timezone.now, verbose_name="Закрывать")

    class Meta:
        verbose_name = "Расположение"
        verbose_name_plural = "Расположение"

    def __str__(self):
        return f"Title: {self.address} Long: {self.longitude} Lat:{self.latitude}"
