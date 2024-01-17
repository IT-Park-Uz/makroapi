from django.contrib import admin
from django.utils.safestring import mark_safe

from common.product.models import Category, Product, File, CatalogFile, TopCategory
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
    list_display = ['title', 'display_image', 'code', 'newPrice', 'oldPrice']
    list_filter = ['title', 'newPrice', 'oldPrice']
    search_fields = ['title', 'newPrice', 'oldPrice']
    exclude = ['created_at']

    def display_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100" height="110" />')

    display_image.short_description = 'Image'
