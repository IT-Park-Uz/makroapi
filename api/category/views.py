from rest_framework.generics import ListAPIView

from api.product.serializers import CategoryCreateSerializer
from common.product.models import Category


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
