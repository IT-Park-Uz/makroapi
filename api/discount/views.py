from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView

from api.discount.serializers import DiscountCreateSerializer, DiscountListSerializer
from api.paginator import CustomPagination
from api.permissions import IsAdmin
from common.discount.models import Discount


class DiscountCreateAPIView(CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountCreateSerializer
    permission_classes = [IsAdmin]


class DiscountListAPIView(ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)

        others = self.request.query_params.get('others')
        guid = self.request.query_params.get('guid')
        product = Discount.objects.filter(guid=guid).first()
        if others and product:
            try:
                queryset = queryset.filter(subcategory=product.subcategory).exclude(guid=guid)
            except:
                pass

        p = self.request.query_params.get('p')
        if p:
            self.pagination_class = CustomPagination
        return queryset


class DiscountDetailAPIView(ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountListSerializer


class DiscountUpdateAPIView(UpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountCreateSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'guid'


class DiscountDeleteAPIView(DestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountCreateSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'guid'
