from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import User


@admin.register(User)
class Useradminmodel(ModelAdmin):
    pass
