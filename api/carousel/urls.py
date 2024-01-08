from django.urls import path

from api.carousel.views import CarouselItemAPIView

app_name = 'carousel'

urlpatterns = [
    path("-list/", CarouselItemAPIView.as_view(), name="carousel_list"),
]
