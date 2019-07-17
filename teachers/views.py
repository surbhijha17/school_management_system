from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Teacher,Assignment
from attendance.models import daily_attendance
from classes.models import ClassInfo
# Create your views here.
@login_required
def teacher_profile(request):
	teachers=Teacher.objects.get(user=request.user)
	classes=teachers.class_info.all()
	a=[]
	for c in classes:
		a.append(daily_attendance.objects.all().filter(class_info=c).filter(teacher=teachers).count())

	return render(request,'teachers/profile.html',{'teachers':teachers,'classes':classes,'a':a})

@login_required
def classes(request):
	teachers=Teacher.objects.all().filter(user=request.user)
	classes=teachers[0].class_info.all()

	return render(request,'teachers/class.html',{'teachers':teachers[0],'classes':classes})
@login_required
def upload_assignment(request):
	teachers=Teacher.objects.all().filter(user=request.user)
	classes=teachers[0].class_info.all()
	assign = Assignment.objects.all().filter(teacher=teachers[0])
	if request.method == 'POST' and request.FILES['assignment']:
		c=request.POST.get('class_info')
		cl=ClassInfo.objects.get(name=c)
		d=request.POST.get('duedate')
		a = request.FILES['assignment']
		Assignment.objects.create(file=a, class_info=cl, duedate=d, teacher=teachers[0])
		return render(request,'teachers/uploadedassignment.html',{'assign':assign,'classes':classes,'teachers':teachers[0]})
	return render(request, 'teachers/upload_assignment.html',{'classes':classes,'teachers':teachers[0]})

def uploaded_assignment(request):
	teachers=Teacher.objects.all().filter(user=request.user)
	classes=teachers[0].class_info.all()
	assign = Assignment.objects.all().filter(teacher=teachers[0])
	return render(request,'teachers/uploadedassignment.html',{'assign':assign,'classes':classes,'teachers':teachers[0]})