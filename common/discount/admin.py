from django.contrib import admin
from django.utils.safestring import mark_safe

from common.discount.models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['startDate', 'endDate', 'display_image', 'status']
    exclude = ['created_at']

    def display_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100" height="110" />')

    display_image.short_description = 'Image'
