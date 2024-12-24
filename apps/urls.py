from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views import UserListAPIView, RegisterAPIView, VerifyEmailAPIView, LoginAPIView, \
    HealthAPIView, MedicalTechnologyAPIView, TechnologyAppointmentAPIView, RoomAPIView, \
    UserDestroyAPIView, HealthDestroyAPIView, MedicalTechnologyDestroyAPIView, TechnologyAppointmentDestroyAPIView, \
    RoomDestroyAPIView, AppointmentAPIView, AppointmentDestroyAPIView

urlpatterns = [
    path('User',UserListAPIView.as_view(), name = 'User'),
    path('register',RegisterAPIView.as_view(), name = 'login-register'),
    path('verify-email/', VerifyEmailAPIView.as_view(), name='verify-email'),
    path('login/', LoginAPIView.as_view(), name='login'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



    path('appoitment', AppointmentAPIView.as_view()),
    # path('appoitment-destroy', AppointmentDestroyAPIView.as_view()),
    path('health', HealthAPIView.as_view()),
    path('medical-technology', MedicalTechnologyAPIView.as_view()),
    path('technology-appoitment', TechnologyAppointmentAPIView.as_view()),
    path('room', RoomAPIView.as_view()),
    path('users/<int:id>/delete/', UserDestroyAPIView.as_view(), name='user-destroy'),
    path('appointments/<int:id>/delete/', AppointmentDestroyAPIView.as_view(), name='appointment-destroy'),
    path('health/<int:id>/delete/', HealthDestroyAPIView.as_view(), name='health-destroy'),
    path('medical-technology/<int:id>/delete/', MedicalTechnologyDestroyAPIView.as_view(),
         name='medical-technology-destroy'),
    path('technology-appointment/<int:id>/delete/', TechnologyAppointmentDestroyAPIView.as_view(),
         name='technology-appointment-destroy'),
    path('rooms/<int:id>/delete/', RoomDestroyAPIView.as_view(), name='room-destroy'),


]

