from rest_framework import serializers

from common.product.models import Product, Category, CatalogFile, TopCategory
from config.settings.base import env


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TopCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopCategory
        fields = ['id', 'title']


class CatalogFileSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    def get_file(self, catalog):
        if catalog.file and not "http" in catalog.file:
            return env('BASE_URL') + catalog.file.url
        return None

    class Meta:
        model = CatalogFile
        fields = ['id', 'title', 'file', 'endDate']


class ProductListSerializer(serializers.ModelSerializer):
    photo_medium = serializers.SerializerMethodField()

    def get_photo_medium(self, product):
        if product.photo and not "http" in product.photo:
            return env('BASE_URL') + product.photo.url
        return None

    class Meta:
        model = Product
        fields = ['id', 'code', 'title', 'photo_medium', 'newPrice', 'oldPrice', 'percent', 'startDate',
                  'endDate', 'status']
