import uuid

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from accounts.models import CustomUser

# Create your views here.
from django.shortcuts import render, redirect
from .models import StudentSkill, StudentSkillRequest
from . import forms

# Create your views here.


@login_required(login_url="/login")
def log_new(request):
    if request.method == 'POST':
        form = forms.LogSkill(request.POST)
        if form.is_valid():
            StudentSkill.objects.update_or_create(
                student=request.user,
                skill=form.cleaned_data['skill'],
                defaults={
                    'level': form.cleaned_data['level'],
                    'instructor': form.cleaned_data['instructor'],
                    'approved': False
                },
            )
            StudentSkillRequest.objects.create(
                student=request.user,
                skill=form.cleaned_data['skill'],
                level=form.cleaned_data['level'],
                instructor=form.cleaned_data['instructor'],
            )
            return redirect('profile')
    else:
        form = forms.LogSkill()
    return render(request, 'skills/log_skills.html', {'form': form})

@login_required(login_url="/login")
def passport(request):
    user_id = request.user.id
    token = str(uuid.uuid4())
    custom_url = f"https://corbinhast.pythonanywhere.com/share/{user_id}/{token}/"
    return render(request, 'skills/passport.html',  {'qr_url': custom_url})

def share(request, user,token):

    student = get_object_or_404(CustomUser,id=user)
    skills = StudentSkill.objects.filter(student=student, approved=1)
    return render(request, 'skills/share.html', {'skills': skills, 'student': student})