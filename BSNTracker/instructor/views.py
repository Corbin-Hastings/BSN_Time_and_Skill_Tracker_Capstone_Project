from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from hour.models import hoursLog
from skills.models import StudentSkill
from instructor.models import Instructor, Course


# Create your views here.
@login_required(login_url='/login/')
def hour_approval(request):
    if request.method == 'POST':
        kind = request.POST.get('kind')
        obj_id = request.POST.get('id')
        action = request.POST.get('action')

        model = hoursLog if kind == 'hours' else StudentSkill
        obj = model.objects.get(pk=obj_id)

        if action == 'approve':
            obj.approved = 1
            obj.save()
        elif action == 'deny':
            obj.approved = 2
            obj.save()

        return redirect(request.path)

    session=request.user.id
    inst = Instructor.objects.get(user_id=session)
    courses = inst.courses.all()

    requests = hoursLog.objects.filter(course__in=courses).filter(approved=0)
    s_requests = StudentSkill.objects.filter(instructor_id=request.user.id).filter(approved=0)
    return render(request, 'hour_approval.html',context={'requests':requests,'s_requests':s_requests})