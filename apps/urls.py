from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views import UserListAPIView, RegisterAPIView, VerifyEmailAPIView, LoginAPIView

urlpatterns = [
    path('User',UserListAPIView.as_view(), name = 'User'),
    path('register',RegisterAPIView.as_view(), name = 'login-register'),
    path('verify-email/', VerifyEmailAPIView.as_view(), name='verify-email'),
    path('login/', LoginAPIView.as_view(), name='login'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

