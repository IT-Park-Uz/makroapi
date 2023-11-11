from django.contrib import admin
from django.utils.safestring import mark_safe

from common.discount.models import Discount, DiscountCatalog


class DiscountCatalogAdmin(admin.TabularInline):
    model = DiscountCatalog
    extra = 0
    readonly_fields = ("get_image_uz", "get_image_ru",)

    def get_image_uz(self, obj):
        return mark_safe(f'<img src={obj.photo_uz.url} width="100" height="100"')

    get_image_uz.short_description = "Узбекская изображение"

    def get_image_ru(self, obj):
        return mark_safe(f'<img src={obj.photo_ru.url} width="100" height="100"')

    get_image_ru.short_description = "Русская изображение"


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['startDate', 'endDate', 'display_image', 'status']
    exclude = ['created_at']
    inlines = [DiscountCatalogAdmin]

    def display_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100" height="110" />')

    display_image.short_description = 'Image'
