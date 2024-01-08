from django.contrib import admin

from common.carousel.models import CarouselItem


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    ...
