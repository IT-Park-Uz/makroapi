from django.urls import path

from api.category.views import CategoryCreateAPIView, CategoryListAPIView, CategoryDetailAPIView


app_name = 'category'

urlpatterns = [
    path("-create/", CategoryCreateAPIView.as_view(), name="category_create"),
    path("-list/", CategoryListAPIView.as_view(), name="category_list"),
    path("-detail/<uuid:guid>/", CategoryDetailAPIView.as_view(), name="category_detail"),
]
