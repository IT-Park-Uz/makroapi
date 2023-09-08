from django.urls import path

from api.location.views import LocationCreateAPIView, LocationListAPIView, LocationDetailAPIView, \
    LocationUpdateAPIView, LocationDeleteAPIView

app_name = 'location'

urlpatterns = [
    path("-create/", LocationCreateAPIView.as_view(), name="location_create"),
    path("-list/", LocationListAPIView.as_view(), name="location_list"),
    path("-detail/<uuid:guid>/", LocationDetailAPIView.as_view(), name="location_detail"),
    path("-update/<uuid:guid>/", LocationUpdateAPIView.as_view(), name="location_update"),
    path("-destroy/<uuid:guid>/", LocationDeleteAPIView.as_view(), name="location_delete"),
]
