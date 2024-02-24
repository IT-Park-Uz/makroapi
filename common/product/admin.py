from django.contrib import admin
from django.utils.safestring import mark_safe

from common.product.models import Category, Product, File, CatalogFile, TopCategory, ProductRegion
from modeltranslation.admin import TabbedTranslationAdmin

admin.site.register(CatalogFile)
admin.site.register(Category)
admin.site.register(TopCategory)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ["pk", 'processed_func']
    list_display_links = ["pk"]
    readonly_fields = ("processed", "total")

    def processed_func(self, obj):
        return f"{obj.processed}/{obj.total}"

    processed_func.short_description = "Обработано/Всего"


@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    list_display = ['title', 'display_image', 'code', 'region', 'newPrice', 'oldPrice', 'endDate', 'status']
    list_display_links = list_display[:-1]
    list_filter = ['category', 'top_category']
    list_editable = ["status"]
    search_fields = ['title', 'newPrice', 'oldPrice']
    exclude = ['created_at']
    ordering = ['photo', 'code']
    date_hierarchy = 'endDate'

    def display_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100" height="110" />')

    display_image.short_description = 'Image'


@admin.register(ProductRegion)
class ProductRegionAdmin(admin.ModelAdmin):
    list_display = ["name_ru", "name_uz"]
