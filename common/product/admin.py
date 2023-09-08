from django.contrib import admin

from common.product.models import Category, Product, File

admin.site.register(File)
admin.site.register(Category)
admin.site.register(Product)
