import logging

from rest_framework import serializers

from common.product.models import Product, Category, CatalogFile, TopCategory, ProductRegion


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
            return request.build_absolute_uri(catalog.file.url)
        return None

    class Meta:
        model = CatalogFile
        fields = ['id', 'title', 'file', 'endDate']


class ProductListSerializer(serializers.ModelSerializer):
    photo_medium = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'code', 'title', 'photo_medium', 'newPrice', 'oldPrice', 'percent', 'startDate',
                  'endDate', 'status']

    def get_photo_medium(self, instance):
        request = self.context.get('request')
        if request and instance.photo:
            photo_absolute_uri = request.build_absolute_uri(instance.photo.url)
            return photo_absolute_uri.replace('http', 'https')
        return None


class ProductRegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRegion
        fields = "__all__"
