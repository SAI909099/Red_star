from datetime import timedelta
from urllib.parse import urlparse

import redis
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.models import User
from root import settings

redis_url = urlparse(settings.CELERY_BROKER_URL)
r = redis.StrictRedis(host=redis_url.hostname, port=redis_url.port, db=int(redis_url.path.lstrip('/')))


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ()

class RegisterSerializer(ModelSerializer):
    password = CharField(write_only=True)
    confirm_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token



class LoginUserModelSerializer(Serializer):
    email = EmailField()
    password = CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        redis_key = f'failed_attempts_{email}'
        attempts = r.get(redis_key)
        if attempts and int(attempts) >= 5:
            raise ValidationError("Too many failed login attempts. Try again after 5 minutes.")

        user = authenticate(email=email, password=password)

        if user is None:
            current_attempts = int(attempts) if attempts else 0
            r.setex(redis_key, timedelta(minutes=5), current_attempts + 1)
            raise ValidationError("Invalid email or password")

        r.delete(redis_key)
        attrs['user'] = user
        return attrs


class LoginSerializer(Serializer):
    email = EmailField()
    verification_code = CharField(write_only=True)

from rest_framework import serializers, viewsets
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .models import User, Appointments, Health, MedicalTechnology, TechnologyAppointment, Room

# Seriali
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = '__all__'

class MedicalTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTechnology
        fields = '__all__'

class TechnologyAppointmentSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # Check if the time slot is already booked
        if TechnologyAppointment.objects.filter(
            technology=data['technology'],
            appointment_date=data['appointment_date'],
            appointment_time=data['appointment_time']
        ).exists():
            raise serializers.ValidationError("This time slot is already booked.")
        return data

    class Meta:
        model = TechnologyAppointment
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
