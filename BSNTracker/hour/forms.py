from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from datetime import datetime, timedelta

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

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        course = cleaned_data.get('course')
        types = cleaned_data.get('types')

        if not start_time or not end_time or not course or not types:
            return cleaned_data


        if end_time <= start_time:
            raise forms.ValidationError("End time is before start time")
        if end_time - start_time >= timedelta(hours=12):
            raise forms.ValidationError("The total time you have entered is more that 12 hours")
        return cleaned_data


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_time'].initial = datetime.now()
        self.fields['end_time'].initial = datetime.now()
