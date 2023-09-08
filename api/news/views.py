from datetime import datetime

from django.db.models import Q
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, DestroyAPIView

from api.news.serializers import NewsCreateSerializer, NewsListSerializer, NewsDetailSerializer
from api.paginator import CustomPagination
from api.permissions import IsAdmin
from common.news.models import News


class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    # permission_classes = [IsAdmin]


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)

        date = self.request.query_params.get('date')  # 2023-09-06
        if date:
            date = datetime.strptime(date, '%Y-%m-%d').date()
            queryset = queryset.filter(startDate__month=date.month)
        others = self.request.query_params.get('others')
        guid = self.request.query_params.get('guid')
        if others and guid:
            try:
                queryset = queryset.exclude(guid=guid)
            except:
                pass
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        p = self.request.query_params.get('p')
        if p:
            self.pagination_class = CustomPagination
        return queryset


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'guid'


class NewsUpdateAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'guid'


class NewsDeleteAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'guid'
