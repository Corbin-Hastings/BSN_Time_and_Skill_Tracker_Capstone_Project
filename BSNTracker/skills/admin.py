from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *

@admin.register(Skills)
class AdminSkillsLog(admin.ModelAdmin):
    list_display = ['user','skill','instructor','approved']
    list_editable = ['skill','approved']
    search_fields = ['user']
