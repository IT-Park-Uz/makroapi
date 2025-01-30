from django.urls import path

from api.files.views import OffertaListAPIView

app_name = 'files'

urlpatterns = [
    path("-list/", OffertaListAPIView.as_view(), name="offerta_list"),
]
