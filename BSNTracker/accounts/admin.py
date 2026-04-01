from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','date_joined','is_staff','is_active']
    list_editable = ['is_staff','is_active']
    search_fields = ['first_name','last_name','email']
