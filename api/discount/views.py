from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView

from api.discount.serializers import DiscountCreateSerializer, DiscountListSerializer, DiscountDetailSerializer
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
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()

        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class DiscountDetailAPIView(RetrieveAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountDetailSerializer


class DiscountUpdateAPIView(UpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountCreateSerializer
    permission_classes = [IsAdmin]


class DiscountDeleteAPIView(DestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountCreateSerializer
    permission_classes = [IsAdmin]
