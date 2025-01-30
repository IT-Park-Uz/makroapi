from rest_framework.generics import ListAPIView

from api.news.serializers import NewsListSerializer
from api.paginator import CustomPagination
from common.files.models import Offerta


class OffertaListAPIView(ListAPIView):
    queryset = Offerta.objects.all()
    serializer_class = NewsListSerializer
    pagination_class = CustomPagination
