from rest_framework.generics import ListAPIView

from api.files.serializers import OffertaListSerializer
from api.paginator import CustomPagination
from common.files.models import Offerta


class OffertaListAPIView(ListAPIView):
    queryset = Offerta.objects.all()
    serializer_class = OffertaListSerializer
    pagination_class = CustomPagination
