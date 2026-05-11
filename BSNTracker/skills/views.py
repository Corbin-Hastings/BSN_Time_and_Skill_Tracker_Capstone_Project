import uuid
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
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
    user = request.user
    user_id = request.user.id
    token = str(uuid.uuid4())

    user.custom_token = token
    user.token_time = timezone.now()

    user.save()

    custom_url = f"https://corbinhast.pythonanywhere.com/share/{user_id}/{token}/"
    return render(request, 'skills/passport.html',  {'qr_url': custom_url})

def share(request, user,token):
    student = get_object_or_404(CustomUser,id=user)

    if student.custom_token != token:
        return HttpResponseForbidden("ERROR")

    if not student.token_time or timezone.now() > student.token_time + timedelta(minutes=60):
        student.custom_token = None
        student.token_time = None
        student.save()
        return HttpResponseForbidden("Invalid or expired token")

    skills = StudentSkill.objects.filter(student=student, approved=True)
    return render(request, 'skills/share.html', {'skills': skills, 'student': student})