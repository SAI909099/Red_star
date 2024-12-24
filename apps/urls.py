from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views import UserListAPIView,AppointmentViewSet, RegisterAPIView, VerifyEmailAPIView, LoginAPIView, HealthViewSet, \
    MedicalTechnologyViewSet, TechnologyAppointmentViewSet, RoomViewSet

router = DefaultRouter()
router.register('appointments', AppointmentViewSet, basename='appointments')
router.register('health', HealthViewSet, basename='health')
router.register('medical-technology', MedicalTechnologyViewSet, basename='medical-technology')
router.register('technology-appointments', TechnologyAppointmentViewSet, basename='technology-appointments')
router.register('rooms', RoomViewSet, basename='rooms')

urlpatterns = [
    path('User',UserListAPIView.as_view(), name = 'User'),
    path('register',RegisterAPIView.as_view(), name = 'login-register'),
    path('verify-email/', VerifyEmailAPIView.as_view(), name='verify-email'),
    path('login/', LoginAPIView.as_view(), name='login'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/', include(router.urls)),
]

