from django.db import models
from common.users.base import BaseModel
from common.discount.models import Discount
from common.news.models import News


class CarouselItem(BaseModel):
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True, blank=True)
    display_order = models.IntegerField(default=0, verbose_name="Порядок отображения")
    url = models.URLField(verbose_name="Ссылка для перехода", null=True, blank=True)
    photo = models.ImageField("Изображение", upload_to='carouselImage', null=True, blank=True)
    photo_mobile = models.ImageField("Изображение для мобилки", upload_to='carouselImageMobile', null=True, blank=True)

    class Meta:
        verbose_name = "Элемент карусели"
        verbose_name_plural = "Элементы карусели"

    def __str__(self):
        if self.discount:
            return f"Элемент карусели: Скидка #{self.discount.title}"
        elif self.news:
            return f"Элемент карусели: Новости #{self.news.title}"
        else:
            return "Элемент карусели"
