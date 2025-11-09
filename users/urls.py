# users/urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserViewSet

urlpatterns = [
    # JWT аутентификация (стандартная)
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Пользователи
    path('register/', UserViewSet.as_view({'post': 'create'}), name='register'),
    path('profile/', UserViewSet.as_view({'get': 'me'}), name='profile'),
]