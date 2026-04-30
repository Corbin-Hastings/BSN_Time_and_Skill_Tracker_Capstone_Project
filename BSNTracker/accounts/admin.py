from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html

from .models import *
from instructor.models import Instructor


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ordering = ("first_name", "last_name")
    list_display = ['first_name','last_name','email','date_joined','is_staff','is_superuser','is_active']
    list_editable = ['is_staff','is_superuser','is_active']
    search_fields = ['first_name','last_name','email']

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


    def password_reset_email(self,obj):
        url = ()
        return format_html('<a href="{}">View skills</a>', url)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.is_staff:
            if Instructor.objects.filter(user_id=obj).exists():
                pass
            else:
                Instructor.objects.create(user_id=obj)

        else:
            Instructor.objects.filter(user_id=obj).delete()

