from django.shortcuts import render, redirect, get_object_or_404
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


