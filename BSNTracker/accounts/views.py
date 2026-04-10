from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from hour.models import hoursLog

from skills.models import StudentSkill

# Create your views here.


def register(request):

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # TODO add the user processing
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = CustomUserCreationForm()

    return render(request,"signup/signup.html",{"form":form})

def login_view(request):

    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
        else:
            return HttpResponseRedirect("/login")
    else:
        form = AuthenticationForm()

    return render(request,"login/login.html",{"form":form})

def logout_view(request):
    logout(request)
    return redirect("/")
@login_required(login_url="/login")
def profile_view(request):
    skills = StudentSkill.objects.filter(student=request.user).order_by('-date')
    hours = hoursLog.objects.filter(user=request.user).order_by('-end_time')

    get_hours = hours.aggregate(Sum('hours'))
    total_hours = get_hours['hours__sum'] or 0

    return render(request, "profile/profile.html", {'skills': skills, 'hours': hours,'total_hours': total_hours})

