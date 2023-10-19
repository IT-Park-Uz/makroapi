from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.generics import ListAPIView

from api.paginator import CustomPagination
from api.product.serializers import CategoryCreateSerializer, TopCategoryCreateSerializer
from common.product.models import Category, TopCategory, Product, ProductStatus
from config.settings.base import CACHE_TTL


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    pagination_class = CustomPagination

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class TopCategoryListAPIView(ListAPIView):
    queryset = TopCategory.objects.filter(
        Top_categoryProducts__in=Product.objects.filter(status=ProductStatus.HasDiscount)).distinct()
    serializer_class = TopCategoryCreateSerializer
    pagination_class = CustomPagination

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
