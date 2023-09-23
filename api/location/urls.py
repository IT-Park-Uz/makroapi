from django.urls import path

from api.location.views import LocationListAPIView, LocationDetailAPIView, \
    RegionListAPIView, DistrictListAPIView

app_name = 'location'

urlpatterns = [
    # path("-create/", LocationCreateAPIView.as_view(), name="location_create"),
    path("-region-list/", RegionListAPIView.as_view(), name="region_list"),
    path("-district-list/", DistrictListAPIView.as_view(), name="district_list"),
    path("-list/", LocationListAPIView.as_view(), name="location_list"),
    # path("-detail/<int:pk>/", LocationDetailAPIView.as_view(), name="location_detail"),
    # path("-update/<int:pk>/", LocationUpdateAPIView.as_view(), name="location_update"),
    # path("-destroy/<int:pk>/", LocationDeleteAPIView.as_view(), name="location_delete"),
]
