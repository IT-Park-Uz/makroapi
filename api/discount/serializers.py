from typing import Optional

from rest_framework import serializers

from common.discount.models import Discount, DiscountCatalog
from config.settings.base import env
from makro_uz.contrib.ckeditor_serializer_fields import FixAbsolutePathSerializer


class DiscountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'photo', 'url', 'startDate', 'endDate', 'status']


class DiscountListSerializer(serializers.ModelSerializer):
    photo_medium = serializers.ImageField(read_only=True)
    file = serializers.SerializerMethodField()

    def get_file(self, catalog) -> Optional[str]:
        if catalog.file and not "http" in catalog.file:
            return env('BASE_URL') + catalog.file.url
        return None

    class Meta:
        model = Discount
        fields = ['id', 'title', 'photo_medium', 'url', 'startDate', 'endDate', 'status', 'titleFile', 'file',
                  'endDateFile', 'photo_mobile']


class DiscountCatalogImagesSerializer(serializers.ModelSerializer):
    photo_uz = serializers.SerializerMethodField()
    photo_ru = serializers.SerializerMethodField()

    def get_photo_uz(self, news) -> Optional[str]:
        if news.photo_uz and not "http" in news.photo_uz:
            return env('BASE_URL') + news.photo_uz.url
        return None

    def get_photo_ru(self, news) -> Optional[str]:
        if news.photo_ru and not "http" in news.photo_ru:
            return env('BASE_URL') + news.photo_ru.url
        return None

    class Meta:
        model = DiscountCatalog
        fields = ['id', 'photo_uz', 'photo_ru']


class DiscountDetailSerializer(serializers.ModelSerializer):
    discountCatalog = DiscountCatalogImagesSerializer(many=True)
    description = FixAbsolutePathSerializer()
    photo_medium = serializers.ImageField(read_only=True)

    class Meta:
        model = Discount
        fields = ['id', 'title', 'description', 'photo_medium', 'url', 'startDate', 'endDate', 'status', 'titleFile',
                  'file', 'endDateFile', 'discountCatalog', 'photo_mobile']
