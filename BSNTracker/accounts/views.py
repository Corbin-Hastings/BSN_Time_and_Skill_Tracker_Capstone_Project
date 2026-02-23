from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CustomUserCreationForm

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
