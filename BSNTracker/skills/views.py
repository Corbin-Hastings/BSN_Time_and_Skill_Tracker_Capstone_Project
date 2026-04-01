from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import StudentSkill
from . import forms

# Create your views here.
def skills_list(request):
    skills = StudentSkill.objects.filter(student=request.user).order_by('-date')
    return render(request, 'skills/skills_list.html', {'skills': skills})

def log_new(request):
    if request.method == 'POST':
        form = forms.LogSkill(request.POST)
        if form.is_valid():
            newskill = form.save(commit=False)
            newskill.student = request.user
            newskill.save()
            return redirect('skills:list')
    else:
        form = forms.LogSkill()
    return render(request, 'skills/log_skills.html', {'form': form})
