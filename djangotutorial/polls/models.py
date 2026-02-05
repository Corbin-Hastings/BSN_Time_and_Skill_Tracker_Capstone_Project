from django.db import models

# Create your models here.
from django.db import models
from django.db.models import Q


class Level(models.TextChoices):
    sim = 's','S'
    assisted = 'a','A'
    independent = 'i','I'
class AccountType(models.TextChoices):
    STUDENT = 'STU'
    INSTRUCTOR = 'INST'
    ADMIN = 'ADMIN'

class User(models.Model):
    name= models.CharField(max_length=64)
    email= models.CharField(max_length=128)
    admin= models.BooleanField(default=False)
    roll= models.CharField(max_length=5,default='STU',choices=AccountType.choices)

class Skill(models.Model):
    skill = models.CharField(max_length=128)# TODO: make this a text choice. this means a new choice class

class StudentSkill(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    skill =models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.CharField(max_length=1,choices=Level.choices)
    date_learned = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('student','skill')
class Skill(models.Model):

    skill = models.CharField(max_length=300)
    level = models.CharField(choices=Level.choices, max_length=2)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(level__in=Level.values),
                name='level_val'
            )
        ]
