import logging

from rest_framework import serializers

from common.product.models import Product, Category, CatalogFile, TopCategory


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
        request = self.context.get('request')
        if catalog.file:
            r = request.build_absolute_uri(catalog.file.url)
            logging.info(r)
            return r
        return None

    class Meta:
        model = CatalogFile
        fields = ['id', 'title', 'file', 'endDate']


class ProductListSerializer(serializers.ModelSerializer):
    photo_medium = serializers.ImageField(source="photo")

    class Meta:
        model = Product
        fields = ['id', 'code', 'title', 'photo_medium', 'newPrice', 'oldPrice', 'percent', 'startDate',
                  'endDate', 'status']
