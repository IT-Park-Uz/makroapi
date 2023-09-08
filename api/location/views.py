from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, DestroyAPIView

from api.location.serializers import LocationCreateSerializer
from api.permissions import IsAdmin
from common.news.models import Location


class LocationCreateAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer
    permission_classes = [IsAdmin]


class LocationListAPIView(ListAPIView):
    queryset = Location.objects.all().order_by('-created_at')
    serializer_class = LocationCreateSerializer


class LocationDetailAPIView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer
    lookup_field = 'guid'


class LocationUpdateAPIView(UpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'guid'


class LocationDeleteAPIView(DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'guid'
