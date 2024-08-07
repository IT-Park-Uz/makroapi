from django_filters import rest_framework as filters
from common.discount.models import Discount


class DiscountFilter(filters.FilterSet):
    is_main = filters.BooleanFilter(field_name='is_main')

    class Meta:
        model = Discount
        fields = ['is_main']
