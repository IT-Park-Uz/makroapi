from rest_framework import serializers
from common.carousel.models import CarouselItem



class CarouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        fields = '__all__'
