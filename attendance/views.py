from django.shortcuts import render,redirect, get_object_or_404
#from .forms import Attendance_form
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from students.models import Student
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import six, timezone
from datetime import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
User=get_user_model()
from classes.models import ClassInfo,Subject
from teachers.models import Teacher
# Create your views here.


@login_required
def take_attendance(request):
	teachers=Teacher.objects.all().filter(user=request.user)
	classes=teachers[0].class_info.all()

	return render(request,'attendance/attendance.html',{'teachers':teachers[0],'classes':classes})
@login_required
def add_attendance(request,pk):
	teachers=Teacher.objects.all().filter(user=request.user)
	students=Student.objects.all()
	#attendance=Attendance.objects.all()
	pr=Teacher.objects.filter(user=request.user)
	class_info=None
	m=None
	if pk:
		class_info=get_object_or_404(ClassInfo,pk=pk)
		students=students.filter(class_info=class_info)
	a=daily_attendance.objects.all().filter(attendance_date=date.today()).filter(teacher=pr[0]).filter(class_info=class_info).count()
	if a!=0:
		m="Attendance already taken on this date u can update your attendance"

	if request.method == 'POST':
		x=request.POST.getlist('present[]')
		student=','.join(x)
		#add_attendance=class_info.daily_attendance_set.create(student=student,class_info=class_info,teacher=pr[0], mark = True)
		add_attendance=daily_attendance(student=student,class_info=class_info,teacher=pr[0], mark = True)
		a=daily_attendance.objects.all().filter(attendance_date=date.today()).filter(teacher=pr[0]).filter(class_info=class_info).count()
		if a==0:
			add_attendance.save()

		return redirect('teachers:profile')
	return render(request,'attendance/add_attendance.html',{'m':m,'teachers':teachers[0],'students':students,'class_info':class_info})

@login_required
def update_attendance(request, pk):
	teachers=Teacher.objects.all().filter(user=request.user)
	teacher=Teacher.objects.all().filter(user=request.user)
	c = get_object_or_404(ClassInfo, pk =pk)
	d = date.today()
	s = c.student_set.all()
	m=None
	attendance=daily_attendance.objects.all().filter(attendance_date=d).filter(teacher=teacher[0]).filter(class_info=c)
	if daily_attendance.objects.all().filter(attendance_date=d).filter(teacher=teacher[0]).filter(class_info=c).count()==0:
		m=" No attendance taken , Please take the attendance in order to Update................ "
	if request.method == 'POST':
		x=request.POST.getlist('present[]')
		print(x)
		student=','.join(x)
		attendance = daily_attendance.objects.all().filter(attendance_date=d).filter(teacher=teacher[0]).filter(class_info=c).update(student = student)
		#attendance.save()
		return redirect('teachers:profile')
	return render(request, 'attendance/update.html',{'d':d,'m':m,'teachers':teachers[0],'teacher':teacher, 'c':c, 'attendance':attendance,'s':s})


@login_required
def show_attendance(request):
	teachers=Teacher.objects.all().filter(user=request.user)
	teacher=Teacher.objects.all().filter(user=request.user)
	classes=teacher[0].class_info.all()
	class_info=None
	date=None
	attendance=None
	c=None
	t=None
	d=None
	if request.method=="POST":
		class_info=request.POST.get('class_info')
		date=request.POST.get('date')
		print(class_info)
		print(date)
		c=get_object_or_404(ClassInfo,name=class_info)
		attendance=daily_attendance.objects.all().filter(teacher=teacher[0]).filter(attendance_date=date).filter(class_info=class_info)
		t=c.name
		d=date
	return render(request,'attendance/show_attendance.html',{'teachers':teachers[0],'classes':classes,'attendance':attendance,'t':t,'d':d,'c':c})
