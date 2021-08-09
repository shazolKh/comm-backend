from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from account.views import (
    CustomUserCreateAPIView,
    LogoutAPIView,
)

urlpatterns = [
    path('register/', CustomUserCreateAPIView.as_view(), name='register'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
]
