from datetime import datetime

from django.db.models import Q, Prefetch
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response

from api.news.serializers import NewsCreateSerializer, NewsListSerializer, NewsDetailSerializer
from api.paginator import CustomPagination
from api.permissions import IsAdmin
from common.news.models import News, NewsCatalog
from config.settings.base import CACHE_TTL


class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    permission_classes = [IsAdmin]


@extend_schema(
    parameters=[
        OpenApiParameter(name="date", type=str),
    ]
)
class NewsListAPIView(ListAPIView):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsListSerializer
    pagination_class = CustomPagination

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        date = self.request.query_params.get('date')
        if date:
            date = datetime.strptime(date, '%Y-%m-%d').date()
            queryset = queryset.filter(created_at__month=date.month, created_at__year=date.year)
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.prefetch_related(
        Prefetch(
            lookup='newsCatalog',
            queryset=NewsCatalog.objects.all()
        )
    ).all()
    serializer_class = NewsDetailSerializer

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class NewsUpdateAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    permission_classes = [IsAdmin]


class NewsDeleteAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    permission_classes = [IsAdmin]
