from django.db.models import Q
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response

from api.paginator import CustomPagination
from api.permissions import IsAdmin
from api.product.serializers import ProductCreateSerializer, ProductListSerializer, UploadFileSerializer
from api.tasks import createProducts
from common.product.models import Product, File


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
        createProducts.apply_async([file.id])
        return Response(status=status.HTTP_200_OK)


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

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
        p = self.request.query_params.get('p')
        if p:
            self.pagination_class = CustomPagination
        return queryset


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'guid'


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAdmin]


class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAdmin]
