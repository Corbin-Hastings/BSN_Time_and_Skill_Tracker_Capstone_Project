from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *

@admin.register(Skill)
class AdminSkillsLog(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(StudentSkill)
class AdminStudentSkill(admin.ModelAdmin):
    list_display = ['student','skill','level','approved','instructor']
    list_editable = ['approved','level']
    search_fields = ['name']
