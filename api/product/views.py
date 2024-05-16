from django.db.models import Q
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from api.paginator import CustomPagination
from api.product.serializers import ProductListSerializer, CatalogFileSerializer, ProductRegionListSerializer
from api.tasks import createProducts
from common.product.models import Product, CatalogFile, ProductStatus, ProductRegion
from django.conf import settings


@extend_schema(responses={200: CatalogFileSerializer})
class CatalogFileAPIView(RetrieveAPIView):
    queryset = CatalogFile.objects.all()

    @method_decorator(cache_page(settings.CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        file = self.queryset.last()
        return Response(CatalogFileSerializer(file, context={'request': request}).data, status=status.HTTP_200_OK)


class ProductRegionListAPIView(ListAPIView):
    queryset = ProductRegion.objects.all()
    serializer_class = ProductRegionListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all().order_by("order")
    serializer_class = ProductListSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        qs = super().get_queryset()
        if settings.STAGE == 'prod':
            return qs.filter(status=ProductStatus.HasDiscount)
        return qs

    @method_decorator(cache_page(settings.CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(Q(category_id=category))

        min = self.request.query_params.get('min')
        max = self.request.query_params.get('max')
        if min and max:
            queryset = queryset.filter(newPrice__range=[min, max])
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(Q(title__icontains=q))

        region = self.request.query_params.get('region')
        if region:
            queryset = queryset.filter(Q(region=region))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, context={'request': self.request}, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, context={'request': self.request}, many=True)
        return Response(serializer.data)


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'pk'

    @method_decorator(cache_page(settings.CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request': self.request})
        return Response(serializer.data)


def upload_products(request, pk):
    createProducts.apply_async([pk])
    return HttpResponse('<h1>Процесс начат!</h1>')
