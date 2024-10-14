from django.urls import path

from api.discount.views import DiscountCreateAPIView, DiscountListAPIView, DiscountUpdateAPIView, DiscountDeleteAPIView, \
    DiscountDetailAPIView

app_name = 'discount'

urlpatterns = [
    # path("-create/", DiscountCreateAPIView.as_view(), name="discount_create"),
    path("-list/", DiscountListAPIView.as_view(), name="discount-list"),
    path("-detail/<int:pk>/", DiscountDetailAPIView.as_view(), name="discount-detail"),
    # path("-update/<int:pk>/", DiscountUpdateAPIView.as_view(), name="discount_update"),
    # path("-destroy/<int:pk>/", DiscountDeleteAPIView.as_view(), name="discount_delete"),
]
