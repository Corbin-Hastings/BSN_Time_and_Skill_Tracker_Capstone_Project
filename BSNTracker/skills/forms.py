from django import forms
from . import models
from instructor.models import Instructor
class LogSkill(forms.ModelForm):
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all(), empty_label="Select Instructor")
    class Meta:
        model = models.Skills
        fields = ['skill', 'sai', 'completed', 'location', 'instructor']