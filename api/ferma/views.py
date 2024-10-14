from rest_framework.generics import ListAPIView
from api.ferma.serializers import ToysListSerializer
from common.ferma.models import Toys


class ToysListAPIView(ListAPIView):
    queryset = Toys.objects.all().order_by("order")
    serializer_class = ToysListSerializer
    pagination_class = None
