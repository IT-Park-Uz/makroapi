from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Region, Location, District


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'title', 'startDate', 'endDate', 'status']
    exclude = ['created_at']

    def display_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100" height="110" />')

    display_image.short_description = 'Image'


class LocationInline(admin.TabularInline):
    model = Location
    extra = 0
    exclude = ['created_at']
    # fields = ['title', 'address', 'startDate', 'endDate']


class DistrictInline(admin.TabularInline):
    model = District
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
