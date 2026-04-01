from django.db import models
from django.conf import settings

class Course(models.Model):
    course_name = models.CharField(max_length=150)
    def __str__(self):
        return f"{self.course_name}"


class Instructor(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=150)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.user_id.first_name} {self.user_id.last_name}"

