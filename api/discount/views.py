from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response

from api.discount.serializers import DiscountCreateSerializer, DiscountListSerializer, DiscountDetailSerializer
from api.paginator import CustomPagination
from api.permissions import IsAdmin
from common.discount.models import Discount, DiscountStatus
from config.settings.base import CACHE_TTL


class DiscountCreateAPIView(CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountCreateSerializer
    permission_classes = [IsAdmin]


class DiscountListAPIView(ListAPIView):
    queryset = Discount.objects.filter(status=DiscountStatus.ACTIVE).all()
    serializer_class = DiscountListSerializer
    pagination_class = CustomPagination

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class DiscountDetailAPIView(RetrieveAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountDetailSerializer

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class DiscountUpdateAPIView(UpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountCreateSerializer
    permission_classes = [IsAdmin]


class DiscountDeleteAPIView(DestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountCreateSerializer
    permission_classes = [IsAdmin]
