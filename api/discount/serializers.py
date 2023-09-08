from rest_framework import serializers

from common.discount.models import Discount


class DiscountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'guid', 'photo', 'url', 'startDate', 'endDate', 'status']


class DiscountListSerializer(serializers.ModelSerializer):
    photo_medium = serializers.ImageField(read_only=True)

    class Meta:
        model = Discount
        fields = ['id', 'guid', 'photo_medium', 'url', 'startDate', 'endDate', 'status']
