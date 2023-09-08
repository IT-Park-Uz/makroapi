from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from common.users.base import BaseModel, BaseMeta


class Discount(BaseModel):
    photo = models.ImageField("Image of Discount", upload_to='discountImage')
    photo_medium = ImageSpecField(source='photo', processors=[ResizeToFill(1463, 420)], format='PNG',
                                  options={'quality': 100})
    photo_small = ImageSpecField(source='photo', processors=[ResizeToFill(1463, 420)], format='PNG',
                                 options={'quality': 100})
    url = models.CharField(max_length=250, null=True, blank=True)
    startDate = models.DateField(default=timezone.now)
    endDate = models.DateField(default=timezone.now)

    class Meta(BaseMeta):
        pass

    def __str__(self):
        return f"Discount #{self.id}"
