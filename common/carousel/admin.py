from django.contrib import admin

from common.carousel.models import CarouselItem
from django.core.cache import cache


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Clear the cache after saving the Discount model
        cache.clear()
