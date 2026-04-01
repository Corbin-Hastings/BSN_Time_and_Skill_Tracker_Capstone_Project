
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *

@admin.register(hoursLog)
class AdminHourLog(admin.ModelAdmin):
    list_display = ['user','start_time','end_time','types','instructor','approved']
    list_editable = ['start_time','end_time','types','instructor','approved']
    search_fields = ['first_name','last_name','email']
