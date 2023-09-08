from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from common.users.base import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class File(BaseModel):
    file = models.FileField(upload_to='uploadFiles')

    def __str__(self):
        return f"ID # {self.id}"


class ProductStatus(models.IntegerChoices):
    HasDiscount = 1, "HasDiscount"
    NoDiscount = 2, "NoDiscount"


class Product(BaseModel):
    category = models.ForeignKey(Category, related_name='categoryProducts', on_delete=models.SET_NULL, null=True,
                                 blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=200)
    photo = models.ImageField("Image of Product", upload_to='productImage', null=True, blank=True)
    photo_medium = ImageSpecField(source='photo', processors=[ResizeToFill(800, 600)], format='PNG',
                                  options={'quality': 100})
    photo_small = ImageSpecField(source='photo', processors=[ResizeToFill(400, 300)], format='PNG',
                                 options={'quality': 100})
    newPrice = models.FloatField(default=0)
    oldPrice = models.FloatField(default=0)
    percent = models.FloatField(default=0)
    startDate = models.DateField(default=timezone.now)
    endDate = models.DateField(default=timezone.now)
    status = models.IntegerField(choices=ProductStatus.choices, default=ProductStatus.HasDiscount)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title
