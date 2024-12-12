from django.contrib import admin
from django.utils.safestring import mark_safe
from django.conf import settings
from modeltranslation.admin import TabbedTranslationAdmin

from common.product.models import Category, Product, File, CatalogFile, TopCategory, ProductRegion

admin.site.register(CatalogFile)

admin.site.register(TopCategory)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "order", "show_link"]
    list_editable = ["order"]

    def show_link(self, obj):
        """Кнопка для перехода на URL категории."""
        url = f"{settings.FRONTEND_URL}/products?category={obj.id}"
        return mark_safe(f'<a class="button" href="{url}" target="_blank">Открыть категорию</a>')

    show_link.short_description = "Ссылка на категорию"


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
    list_display = ['title', 'display_image', 'code', 'region', 'newPrice', 'promo_type', 'endDate', 'status', 'order']
    list_display_links = list_display[:-2]
    list_filter = ['category', 'top_category', 'promo_type']
    list_editable = ["status", "order", "promo_type"]
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
