from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from common.users.base import BaseModel, BaseMeta


class NewsStatus(models.IntegerChoices):
    ACTIVE = 1, "ACTIVE"
    ARCHIVE = 2, "ARCHIVE"


class News(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    videoURL = models.URLField(null=True, blank=True)
    photo = models.ImageField(_("Image of News"), upload_to='newsImage')
    photo_medium = ImageSpecField(source='photo', processors=[ResizeToFill(1200, 350)], format='PNG',
                                  options={'quality': 90})
    photo_small = ImageSpecField(source='photo', processors=[ResizeToFill(400, 400)], format='PNG',
                                 options={'quality': 90})
    status = models.IntegerField(choices=NewsStatus.choices, default=NewsStatus.ACTIVE)
    startDate = models.DateField(default=timezone.now().date())
    endDate = models.DateField(default=timezone.now().date())

    class Meta(BaseMeta):
        pass

    def __str__(self):
        return self.title


class Region(BaseModel):
    title = models.CharField(max_length=150)

    def __str__(self):
        return f"Title: {self.title}"


class Location(BaseModel):
    region = models.ForeignKey(Region, related_name="regionLocation", on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=300)
    longitude = models.CharField(max_length=60, null=True, blank=True)
    latitude = models.CharField(max_length=60, null=True, blank=True)
    open = models.TimeField(default=timezone.now().time())
    close = models.TimeField(default=timezone.now().time())

    def __str__(self):
        return f"Title: {self.address} Long: {self.longitude} Lat:{self.latitude}"
