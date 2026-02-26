from django.shortcuts import render, HttpResponse



# Create your views here.

def home(request):
    if request.user.is_authenticated:
        name = request.user.first_name
        greet = f"Welcome back,{name} "

    else:
        greet = "Please log in!"

    return render(request,"home.html",{"greet":greet})