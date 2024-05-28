from rest_framework import serializers
from common.carousel.models import CarouselItem


class CarouselItemSerializer(serializers.ModelSerializer):
    news_photo = serializers.ImageField(source="news.photo_medium", allow_null=True)
    discount_photo = serializers.ImageField(source="discount.photo_medium", allow_null=True)
    news_photo_mobile = serializers.ImageField(source="news.photo_medium_mobile", allow_null=True)
    discount_photo_mobile = serializers.ImageField(source="discount.photo_medium_mobile", allow_null=True)

    class Meta:
        model = CarouselItem
        fields = '__all__'
