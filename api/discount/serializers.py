from rest_framework import serializers

from common.discount.models import Discount
from config.settings.base import env


class DiscountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'photo', 'url', 'startDate', 'endDate', 'status']


class DiscountListSerializer(serializers.ModelSerializer):
    photo_medium = serializers.ImageField(read_only=True)
    file = serializers.SerializerMethodField()

    def get_file(self, catalog):
        if catalog.file and not "http" in catalog.file:
            return env('BASE_URL') + catalog.file.url
        return None

    class Meta:
        model = Discount
        fields = ['id', 'title', 'photo_medium', 'url', 'startDate', 'endDate', 'status', 'titleFile', 'file',
                  'endDateFile']


class DiscountDetailSerializer(serializers.ModelSerializer):
    photo_medium = serializers.ImageField(read_only=True)

    class Meta:
        model = Discount
        fields = ['id', 'title', 'description', 'photo_medium', 'url', 'startDate', 'endDate', 'status']
