from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *
from instructor.models import Instructor


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','date_joined','is_staff','is_superuser','is_active']
    list_editable = ['is_staff','is_superuser','is_active']
    search_fields = ['first_name','last_name','email']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.is_staff:
            Instructor.objects.create(user_id=obj)

        else:
            Instructor.objects.filter(user_id=obj).delete()

