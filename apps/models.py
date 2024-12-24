import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import BooleanField, CharField, DateField, Model, IntegerField, ForeignKey, CASCADE, EmailField, \
    FileField, SET_NULL
from django.db.models.fields import DateTimeField, DecimalField, TimeField
from django.utils.timezone import now

from apps.manager import CustomUserManager

class User(AbstractUser):
    username = None
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    date_of_birth = DateField(null=True, blank=True)
    phone_number = CharField(max_length=15,null=True , blank=True)
    address = CharField(max_length=250, blank=True, null=True)
    email = EmailField(unique=True)
    is_active = BooleanField(default=False)
    reset_token = CharField(max_length=64, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Appointments(Model):
    STATUS_CHOICES = [
        ('band qilingan', 'Band qilingan'),
        ('tugallangan', 'Tugallangan'),
        ('bekorqilingan', 'Bekorqilingan'),
    ]

    user = ForeignKey(User, on_delete=CASCADE)
    date = DateTimeField(auto_now_add=True)
    status = CharField(max_length=20, choices=STATUS_CHOICES, default='band qilingan')
    payment_status = BooleanField(default=False)
    payment_method = CharField(max_length=50, blank=True, null=True)
    payment_amount = DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.status} - {self.date}"

class Health(Model):
    user = ForeignKey(User , CASCADE)
    file = FileField(blank=True, null=True)
    Description = CharField(max_length=1000)
    date_added = DateTimeField(auto_now=True)


class MedicalTechnology(Model):
    name = CharField(max_length=100)
    availability_start = TimeField(default=now)
    availability_end = TimeField(default=now)
    is_available = BooleanField(default=True)

class TechnologyAppointment(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    technology = ForeignKey(MedicalTechnology, on_delete=CASCADE)
    appointment_date = DateField(default=now)
    appointment_time = TimeField(default=now)
    status = CharField(max_length=20, choices=[('band qilingan', 'Band qilingan'), ('Tugallangan', 'Tugallangan')])

class Room(Model):
    room_number = CharField(max_length=10, unique=True)
    is_occupied = BooleanField(default=False)
    patient = ForeignKey(User, null=True, blank=True, on_delete=SET_NULL)
    check_in_date = DateField(null=True, blank=True)
    check_out_date = DateField(null=True, blank=True)

    def days_occupied(self):
        if self.is_occupied and self.check_in_date:
            return (datetime.date.today() - self.check_in_date).days
        return 0
