from django.urls import path

from api.news.views import NewsListAPIView, NewsDetailAPIView

app_name = 'news'

urlpatterns = [
    path("-list/", NewsListAPIView.as_view(), name="news_list"),
    path("-detail/<int:pk>/", NewsDetailAPIView.as_view(), name="news_detail"),
]
