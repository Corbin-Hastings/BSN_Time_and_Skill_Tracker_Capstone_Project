from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from datetime import datetime

from .models import hoursLog
from instructor.models import Instructor


# TODO add check to make sure that stat time is before end time.
# TODO check for overlapping entries

class HourInputForm(forms.ModelForm):
    #instructor = forms.ModelChoiceField(queryset=Instructor.objects.all(),empty_label="Select Instructor")
    class Meta:
        model = hoursLog
        fields = ['start_time', 'end_time','course','types']

        widgets = {
            'start_time': forms.DateTimeInput(format='%Y-%m-%d %H:%M',attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'end_time': forms.DateTimeInput(format='%Y-%m-%d %H:%M',attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_time'].initial = datetime.now()
        self.fields['end_time'].initial = datetime.now()
