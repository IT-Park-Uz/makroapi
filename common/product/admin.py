from django.contrib import admin
from django.utils.safestring import mark_safe

from common.product.models import Category, Product, File, CatalogFile

admin.site.register(File)
admin.site.register(CatalogFile)
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_image', 'code', 'newPrice', 'oldPrice']
    list_filter = ['title', 'newPrice', 'oldPrice']
    search_fields = ['title', 'newPrice', 'oldPrice']
    exclude = ['created_at']

    def display_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100" height="110" />')

    display_image.short_description = 'Image'
