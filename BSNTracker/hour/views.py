from django.shortcuts import render,redirect
from .models import hoursLog
from django.contrib.auth.decorators import login_required
from .forms import HourInputForm
@login_required(login_url="/login")
def input_view(request):

    if request.method == "POST":
        form = HourInputForm(request.POST)
        if form.is_valid():
            filled = form.save(commit=False)
            filled.user = request.user
            filled.save()
            return redirect("/")
        else:
            redirect("/")
    else:
        form=HourInputForm()

    return render(request, 'time_entry.html',{"form":form})
@login_required(login_url="/login")
def hours(request):
    entries = hoursLog.objects.filter(user_id = request.user)
    return render(request, 'viewhours.html', {"entries": entries})

@login_required(login_url="/login")
def passport(request):
    return render(request, 'passport.html')

def share(request):
    return render(request, 'share.html')