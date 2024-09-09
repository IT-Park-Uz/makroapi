from rest_framework import generics
from common.carousel.models import CarouselItem
from api.carousel.serializers import CarouselItemSerializer

class CarouselItemAPIView(generics.ListAPIView):
    queryset = CarouselItem.objects.select_related("discount", "news").order_by('display_order')
    serializer_class = CarouselItemSerializer
