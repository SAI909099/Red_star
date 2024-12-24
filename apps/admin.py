from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import User, Appointments, Health, MedicalTechnology, TechnologyAppointment, Room


@admin.register(User)
class Useradminmodel(ModelAdmin):
    pass

@admin.register(Appointments)
class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'status', 'payment_status', 'payment_amount']
    list_filter = ['status', 'payment_status']
    search_fields = ['user__email']

@admin.register(Health)
class HealthAdmin(ModelAdmin):
    pass

@admin.register(MedicalTechnology)
class MedicalTechnologyAdmin(ModelAdmin):
    pass

@admin.register(TechnologyAppointment)
class TechnologyAppointmentAdmin(ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(ModelAdmin):
    pass




