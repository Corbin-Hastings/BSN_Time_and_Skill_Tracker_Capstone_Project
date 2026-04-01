from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *

@admin.register(Skill)
class AdminSkillsLog(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
