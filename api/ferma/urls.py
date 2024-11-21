from django.urls import path

from api.ferma.views import ToysListAPIView

app_name = 'ferma'

urlpatterns = [
    path("-list/", ToysListAPIView.as_view(), name="toys_list"),
]
