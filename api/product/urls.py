from django.urls import path

from api.product.views import ProductCreateAPIView, ProductListAPIView, ProductUpdateAPIView, ProductDeleteAPIView, \
    FileUploadAPIView, ProductDetailAPIView

app_name = 'product'

urlpatterns = [
    # path("-create/", ProductCreateAPIView.as_view(), name="product_create"),
    path("-list/", ProductListAPIView.as_view(), name="product_list"),
    path("-detail/<int:pk>/", ProductDetailAPIView.as_view(), name="product_detail"),
    # path("-update/<uuid:guid>/", ProductUpdateAPIView.as_view(), name="product_update"),
    # path("-destroy/<uuid:guid>/", ProductDeleteAPIView.as_view(), name="product_delete"),

    # path("-file-upload/", FileUploadAPIView.as_view(), name="upload_file"),
]
