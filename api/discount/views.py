from django.db.models import Prefetch
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response

from api.discount.filters import DiscountFilter
from api.discount.serializers import DiscountCreateSerializer, DiscountListSerializer, DiscountDetailSerializer
from api.paginator import CustomPagination
from api.permissions import IsAdmin
from common.discount.models import Discount, DiscountStatus, DiscountCatalog, DiscountFiles
from django.conf import settings
from api.tasks import process_discount_view


class DiscountCreateAPIView(CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountCreateSerializer
    permission_classes = [IsAdmin]


class DiscountListAPIView(ListAPIView):
    queryset = Discount.objects.filter(status=DiscountStatus.ACTIVE, hide=False).all()
    serializer_class = DiscountListSerializer
    pagination_class = CustomPagination
    filterset_class = DiscountFilter

    @method_decorator(cache_page(settings.CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class DiscountDetailAPIView(RetrieveAPIView):
    queryset = Discount.objects.prefetch_related(
        Prefetch(
            lookup='discountCatalog',
            queryset=DiscountCatalog.objects.all()
        ),
        Prefetch(
            lookup='files',
            queryset=DiscountFiles.objects.all()
        )
    ).all()
    serializer_class = DiscountDetailSerializer
    lookup_field = 'pk'

    @method_decorator(cache_page(settings.CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        ip_address = self.get_client_ip(request)
        process_discount_view.delay(instance.id, ip_address)
        return Response(serializer.data)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class DiscountUpdateAPIView(UpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountCreateSerializer
    permission_classes = [IsAdmin]


class DiscountDeleteAPIView(DestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountCreateSerializer
    permission_classes = [IsAdmin]
