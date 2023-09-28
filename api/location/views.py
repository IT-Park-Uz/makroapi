from django.db.models import Prefetch
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response

from api.location.serializers import LocationCreateSerializer, RegionCreateSerializer, DistrictCreateSerializer
from api.paginator import CustomPagination
from api.permissions import IsAdmin
from common.news.models import Location, Region, District
from config.settings.base import CACHE_TTL


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionCreateSerializer
    pagination_class = CustomPagination

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.prefetch_related(
            Prefetch(
                "regionDistrict",
                queryset=District.objects.all(),
                to_attr="districts"
            )
        )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictCreateSerializer
    pagination_class = CustomPagination

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class LocationCreateAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer
    permission_classes = [IsAdmin]


@extend_schema(
    parameters=[
        OpenApiParameter(name="region", type=int),
        OpenApiParameter(name="district", type=int),
    ]
)
class LocationListAPIView(ListAPIView):
    queryset = Location.objects.select_related('district', 'district__region').all()
    serializer_class = LocationCreateSerializer
    pagination_class = CustomPagination

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def get_queryset(self):
        queryset = super().get_queryset()
        district = self.request.query_params.get('district')
        if district:
            queryset = queryset.filter(district=district)
        region = self.request.query_params.get('region')
        if region:
            queryset = queryset.filter(district__region=region)
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
