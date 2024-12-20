from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.generics import ListAPIView

from api.paginator import CustomPagination
from api.product.serializers import CategoryCreateSerializer, TopCategoryCreateSerializer
from common.product.models import Category, TopCategory, Product, ProductStatus
from django.conf import settings


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.filter(
        categoryProducts__in=Product.objects.filter(status=ProductStatus.HasDiscount),
        is_hide=False
    ).order_by('order').distinct()
    serializer_class = CategoryCreateSerializer
    pagination_class = CustomPagination

    @method_decorator(cache_page(settings.CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        if settings.STAGE != 'prod':
            qs = Category.objects.all()
        region_id = self.request.query_params.get('region')
        if region_id:
            qs = qs.filter(categoryProducts__region_id=region_id).distinct()
        return qs


class TopCategoryListAPIView(ListAPIView):
    queryset = TopCategory.objects.filter(
        Top_categoryProducts__in=Product.objects.filter(status=ProductStatus.HasDiscount)).order_by('-id').distinct()
    serializer_class = TopCategoryCreateSerializer
    pagination_class = CustomPagination

    @method_decorator(cache_page(settings.CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
