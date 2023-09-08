from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from api.auth.views import LogoutView, LoginAPIView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name="logout"),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
