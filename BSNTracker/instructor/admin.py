from django.contrib import admin
from .models import *

class CourseSelectionInLine(admin.TabularInline):
    model = Instructor.courses.through
    extra = 1

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    inlines = [CourseSelectionInLine]
    list_display = ['user_id','location']
    filter_horizontal = ['courses']
    search_fields = ['user_id','location']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','course_name']
    list_editable = ['course_name']
    search_fields = ['course_name']
