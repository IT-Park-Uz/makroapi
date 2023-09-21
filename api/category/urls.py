from django.urls import path

from api.category.views import CategoryListAPIView

app_name = 'category'

urlpatterns = [
    path("-list/", CategoryListAPIView.as_view(), name="category_list"),
]
