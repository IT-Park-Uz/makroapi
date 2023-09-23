from rest_framework import serializers

from common.product.models import Product, Category, File
from config.settings.base import env


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class UploadFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)

    class Meta:
        model = File
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'code', 'title', 'photo', 'newPrice', 'oldPrice', 'percent', 'startDate',
                  'endDate', 'status']


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryCreateSerializer()
    # photo_medium = serializers.ImageField(read_only=True)
    photo_medium = serializers.SerializerMethodField()

    def get_photo_medium(self, product):
        if product.photo and not "http" in product.photo:
            return env('BASE_URL') + product.photo.url
        return None

    class Meta:
        model = Product
        fields = ['id', 'category', 'code', 'title', 'photo_medium', 'newPrice', 'oldPrice', 'percent', 'startDate',
                  'endDate', 'status']
