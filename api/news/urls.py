from django.urls import path

from api.news.views import NewsCreateAPIView, NewsListAPIView, NewsDetailAPIView, \
    NewsUpdateAPIView, NewsDeleteAPIView

app_name = 'news'

urlpatterns = [
    # path("-create/", NewsCreateAPIView.as_view(), name="news_create"),
    path("-list/", NewsListAPIView.as_view(), name="news_list"),
    path("-detail/<int:pk>/", NewsDetailAPIView.as_view(), name="news_detail"),
    # path("-update/<int:pk>/", NewsUpdateAPIView.as_view(), name="news_update"),
    # path("-destroy/<int:pk>/", NewsDeleteAPIView.as_view(), name="news_delete"),
]
