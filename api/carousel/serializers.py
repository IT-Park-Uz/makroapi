from rest_framework import serializers
from common.carousel.models import CarouselItem


class CarouselItemSerializer(serializers.ModelSerializer):
    news_photo = serializers.ImageField(source="news.photo_medium", allow_null=True)
    discount_photo = serializers.ImageField(source="discount.photo_medium", allow_null=True)
    news_photo_mobile = serializers.ImageField(source="news.photo_mobile", allow_null=True)
    discount_photo_mobile = serializers.ImageField(source="discount.photo_mobile", allow_null=True)
    news_photo_app = serializers.ImageField(source="news.photo_app", allow_null=True)
    discount_photo_app = serializers.ImageField(source="discount.photo_app", allow_null=True)
    discount_url = serializers.URLField(source="discount.url", allow_null=True)
    news_url = serializers.URLField(source="news.url", allow_null=True)

    class Meta:
        model = CarouselItem
        fields = '__all__'
