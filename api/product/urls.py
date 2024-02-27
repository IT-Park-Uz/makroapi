from django.urls import path

from api.product.views import ProductListAPIView, ProductDetailAPIView, CatalogFileAPIView, ProductRegionListAPIView

app_name = 'product'

urlpatterns = [
    path("-list/", ProductListAPIView.as_view(), name="product_list"),
    path("-region-list/", ProductRegionListAPIView.as_view(), name="product_region_list"),
    path("-detail/<int:pk>/", ProductDetailAPIView.as_view(), name="product_detail"),
    path("-catalog-file/", CatalogFileAPIView.as_view(), name="catalog_file"),
]
