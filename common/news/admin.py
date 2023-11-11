from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Region, Location, District, NewsCatalog


class NewsCatalogAdmin(admin.TabularInline):
    model = NewsCatalog
    extra = 0
    readonly_fields = ("get_image_uz", "get_image_ru",)

    def get_image_uz(self, obj):
        return mark_safe(f'<img src={obj.photo_uz.url} width="100" height="100"')

    get_image_uz.short_description = "Узбекская изображение"

    def get_image_ru(self, obj):
        return mark_safe(f'<img src={obj.photo_ru.url} width="100" height="100"')

    get_image_ru.short_description = "Русская изображение"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_image', 'created_at']
    inlines = [NewsCatalogAdmin]

    def display_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100" height="110" />')

    display_image.short_description = 'Image'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    exclude = ['created_at']


class LocationInline(admin.TabularInline):
    model = Location
    extra = 0
    exclude = ['created_at']
    # fields = ['title', 'address', 'startDate', 'endDate']


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_filter = ['title']
    exclude = ['created_at']
    inlines = [LocationInline]


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_filter = ['title']
    exclude = ['created_at']
