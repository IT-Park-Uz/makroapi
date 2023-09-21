from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, DestroyAPIView

from api.location.serializers import LocationCreateSerializer, RegionCreateSerializer
from api.permissions import IsAdmin
from common.news.models import Location, Region


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionCreateSerializer


class LocationCreateAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer
    permission_classes = [IsAdmin]


class LocationListAPIView(ListAPIView):
    queryset = Location.objects.select_related('region').all()
    serializer_class = LocationCreateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        region = self.request.query_params.get('region')
        if region:
            queryset = queryset.filter(region=region)
        return queryset


class LocationDetailAPIView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer


class LocationUpdateAPIView(UpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer
    permission_classes = [IsAdmin]


class LocationDeleteAPIView(DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer
    permission_classes = [IsAdmin]
