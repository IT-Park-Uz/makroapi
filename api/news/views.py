from datetime import datetime

from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, DestroyAPIView

from api.news.serializers import NewsCreateSerializer, NewsListSerializer, NewsDetailSerializer
from api.paginator import CustomPagination
from api.permissions import IsAdmin
from common.news.models import News


class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    permission_classes = [IsAdmin]


@extend_schema(
    parameters=[
        OpenApiParameter(name="date", pattern="2023-09-06", type=str),
    ]
)
class NewsListAPIView(ListAPIView):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsListSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.query_params.get('date')  # 2023-09-06
        if date:
            date = datetime.strptime(date, '%Y-%m-%d').date()
            queryset = queryset.filter(startDate__month=date.month)
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        return queryset


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer


class NewsUpdateAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    permission_classes = [IsAdmin]


class NewsDeleteAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    permission_classes = [IsAdmin]
