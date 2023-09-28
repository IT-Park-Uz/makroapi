from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response

from api.paginator import CustomPagination
from api.permissions import IsAdmin
from api.product.serializers import ProductCreateSerializer, ProductListSerializer, UploadFileSerializer, \
    CatalogFileSerializer
from api.tasks import createProducts
from common.product.models import Product, File, CatalogFile
from config.settings.base import CACHE_TTL


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAdmin]


class FileUploadAPIView(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = UploadFileSerializer
    permission_classes = [IsAdmin]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.save()
        if not file.isCatalog:
            createProducts.apply_async([file.id])
        return Response(status=status.HTTP_200_OK)


@extend_schema(responses={200: CatalogFileSerializer})
class CatalogFileAPIView(RetrieveAPIView):
    queryset = CatalogFile.objects.all()

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        file = self.queryset.last()
        return Response(CatalogFileSerializer(file).data, status=status.HTTP_200_OK)


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomPagination

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        min = self.request.query_params.get('min')
        max = self.request.query_params.get('max')
        if min and max:
            queryset = queryset.filter(newPrice__range=[min, max])
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(Q(title__icontains=q))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'guid'

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAdmin]


class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAdmin]
