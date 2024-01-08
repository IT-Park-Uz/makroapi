from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = "api"
urlpatterns = router.urls
urlpatterns += [
    path('discount', include("api.discount.urls")),
    path('product', include("api.product.urls")),
    path('news', include("api.news.urls")),
    path('location', include("api.location.urls")),
    path('category', include("api.category.urls")),
    path('carousel', include("api.carousel.urls"))
]
