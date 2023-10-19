from django.urls import path

from api.category.views import CategoryListAPIView, TopCategoryListAPIView

app_name = 'category'

urlpatterns = [
    path("-list/", CategoryListAPIView.as_view(), name="category_list"),
    path("-top-list/", TopCategoryListAPIView.as_view(), name="category_top_list"),
]
