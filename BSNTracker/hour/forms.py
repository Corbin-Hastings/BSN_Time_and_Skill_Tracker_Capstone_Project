from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import hoursLog
from instructor.models import Instructor


# TODO add check to make sure that stat time is before end time.
# TODO check for overlapping entries

class HourInputForm(forms.ModelForm):
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all(),empty_label="Select Instructor")
    class Meta:
        model = hoursLog
        fields = ['start_time', 'end_time', 'location','instructor']

        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'location': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
        }
