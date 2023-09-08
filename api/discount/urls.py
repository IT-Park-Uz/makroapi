from django.urls import path

from api.discount.views import DiscountCreateAPIView, DiscountListAPIView, DiscountUpdateAPIView, DiscountDeleteAPIView

app_name = 'discount'

urlpatterns = [
    path("-create/", DiscountCreateAPIView.as_view(), name="discount_create"),
    path("-list/", DiscountListAPIView.as_view(), name="discount_list"),
    path("-detail/", DiscountListAPIView.as_view(), name="discount_detail"),
    path("-update/<uuid:guid>/", DiscountUpdateAPIView.as_view(), name="discount_update"),
    path("-destroy/<uuid:guid>/", DiscountDeleteAPIView.as_view(), name="discount_delete"),
]
