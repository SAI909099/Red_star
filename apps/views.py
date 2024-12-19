from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, ListCreateAPIView

from apps.models import User
from apps.serializers import UserModelSerializer, RegisterModelSerializer


@extend_schema(tags=['User'])
class UserListAPIView(ListAPIView):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

@extend_schema(tags=['Login-Registe'])
class RegisterListCreateAPIView(ListCreateAPIView):
    serializer_class = RegisterModelSerializer
    queryset = User.objects.all()