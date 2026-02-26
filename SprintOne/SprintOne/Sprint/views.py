from django.shortcuts import render
from .models import hoursLog

def home(request):
    return render(request, 'home.html')

def hours(request):
    items = hoursLog.objects.all()
    return render(request, 'viewhours.html', {"hoursLog": items})