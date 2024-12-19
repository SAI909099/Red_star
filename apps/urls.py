from django.contrib import admin
from django.urls import path, include

from apps.views import UserListAPIView, RegisterListCreateAPIView

urlpatterns = [
    path('User',UserListAPIView.as_view(), name = 'User'),
    path('register',RegisterListCreateAPIView.as_view(), name = 'login-register'),
]

