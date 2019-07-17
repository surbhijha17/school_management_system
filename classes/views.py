from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from teachers.models import Teacher
from students.models import Student
from .models import ClassInfo

@login_required
def show_byclass(request,pk):
	class_infos=ClassInfo.objects.all()
	students=Student.objects.all()
	#attendance=Attendance.objects.all()
	teachers=Teacher.objects.filter(user=request.user)
	class_info=None
	if pk:
		class_info=get_object_or_404(ClassInfo,pk=pk)
		students=students.filter(class_info=class_info)
	return render(request,'classes/byclass.html',{'teachers':teachers[0],'students':students,'class_info':class_info})
