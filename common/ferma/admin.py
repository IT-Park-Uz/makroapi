from django.contrib import admin
from django.utils.safestring import mark_safe

from common.ferma.models import Toys


@admin.register(Toys)
class ToysAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_image', 'order']
    list_editable = ["order"]

    def display_image(self, obj):
        if obj.picture:
            return mark_safe(f'<img src="{obj.picture.url}" width="100" height="100" />')

    display_image.short_description = 'Image'
