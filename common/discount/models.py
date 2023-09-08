from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from common.users.base import BaseModel, BaseMeta


class DiscountStatus(models.IntegerChoices):
    ACTIVE = 1, "ACTIVE"
    ARCHIVE = 2, "ARCHIVE"


class Discount(BaseModel):
    photo = models.ImageField("Image of Discount", upload_to='discountImage')
    photo_medium = ImageSpecField(source='photo', processors=[ResizeToFill(1463, 420)], format='PNG',
                                  options={'quality': 100})
    photo_small = ImageSpecField(source='photo', processors=[ResizeToFill(1463, 420)], format='PNG',
                                 options={'quality': 100})
    url = models.CharField(max_length=250, null=True, blank=True)
    status = models.IntegerField(choices=DiscountStatus.choices, default=DiscountStatus.ACTIVE)
    startDate = models.DateField(default=timezone.now().date())
    endDate = models.DateField(default=timezone.now().date())

    class Meta(BaseMeta):
        pass

    def __str__(self):
        return f"Discount #{self.id}"
