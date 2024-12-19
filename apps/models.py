from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import BooleanField, CharField, DateField, Model, IntegerField, ForeignKey, CASCADE

from apps.manager import CustomUserManager

class User(AbstractUser):
    username = None
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    date_of_birth = DateField(null=True, blank=True)
    phone_number = CharField(max_length=15, unique=True)
    address = CharField(max_length=250, blank=True, null=True)
    is_doctor = BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']

    objects = CustomUserManager()


class Bed(Model):
    name = CharField(max_length=100)
    room_number = CharField(max_length=100)
    phone_number = CharField(max_length=100)
    address = CharField(max_length=100)
    add_tereopy = CharField(max_length=100)
    which_Doctor = ForeignKey(User , CASCADE)


