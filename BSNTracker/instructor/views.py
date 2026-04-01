from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from hour.models import hoursLog
from skills.models import StudentSkill
from instructor.models import Instructor, Course


# Create your views here.
@login_required(login_url='/login/')
def hour_approval(request):
    if request.method == 'POST':
        approved = request.POST.getlist('approvals')
        approved_skills = request.POST.getlist('skills')
        for a in approved:
            obj = hoursLog.objects.get(id=a)
            obj.approved = 1
            obj.save()
        for s in approved_skills:
            obj = StudentSkill.objects.get(pk=s)
            obj.approved = 1
            obj.save()

    session=request.user.id
    inst = Instructor.objects.get(user_id=session)
    courses = inst.courses.all()

    requests = hoursLog.objects.filter(course__in=courses).filter(approved=0)
    s_requests = StudentSkill.objects.filter(instructor_id=request.user.id).filter(approved=0)
    return render(request, 'hour_approval.html',context={'requests':requests,'s_requests':s_requests})