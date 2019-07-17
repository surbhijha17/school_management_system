from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from attendance.models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from teachers.models import Assignment,Teacher
# Create your views here.

@login_required
def students(request):
    s = Student.objects.all().filter(user = request.user)
    return render(request, 'students/profile.html', {'s':s[0]})
@login_required
def profile_base(request):
    s = Student.objects.all().filter(user = request.user)
    return render(request, 'students/profile_base.html', {'s':s[0]})

@login_required
def simple_upload(request):
    s = get_object_or_404(Student, user=request.user)
    c=s.class_info
    roll=s.roll_no
    if request.method == 'POST' and request.FILES['marksheet'] and request.FILES['address'] and request.FILES['identity']:
        marksheet = request.FILES['marksheet']
        a=Document.objects.create(document=marksheet, name = 'C'+str(c)+'/'+str(roll)+'/'+'marksheet')
        address = request.FILES['address']
        b=Document.objects.create(document=address,  name = 'C'+str(c)+'/'+str(roll)+'/'+'address')
        identity = request.FILES['identity']
        c=Document.objects.create(document=identity, name = 'C'+str(c)+'/'+str(roll)+'/'+'identity')
        s.document.add(a)
        s.document.add(b)
        s.document.add(c)
    return render(request, 'students/upload_document.html',{'s':s})

@login_required
def dayAttendance(request):
    s=get_object_or_404(Student,user=request.user)
    c=s.class_info
    print(c)
    t =Teacher.objects.all().filter(class_info=c)
    sub = []
    for i in t:
        sub.append(i.subject)
        print(sub)
    attendance = None
    d=None
    i=None
    if request.method == 'POST':
        i=request.POST.get('subject')
        subject=Subject.objects.all().filter(subject=i)

        d = request.POST.get('date')
        t=Teacher.objects.all().filter(class_info=c).filter(subject=subject[0])
        #t =t.filter(subject=sub)
        attendance=daily_attendance.objects.all().filter(attendance_date=d).filter(teacher = t[0])
    return render(request, 'students/dayAttendance.html',{'sub':sub, 'attendance':attendance, 's':s,'d':d,'i':i})


@login_required
def totalAttendance(request):
    s=get_object_or_404(Student,user=request.user)
    c=s.class_info
    t =Teacher.objects.all().filter(class_info=c)
    sub = []
    for i in t:
        sub.append(i.subject)
    i=None
    totalAttendance=0
    present =0
    if request.method == 'POST':
        i=request.POST.get('subject')
        subject=Subject.objects.all().filter(subject=i)
        #d = request.POST.get('date')
        t=Teacher.objects.all().filter(class_info=c).filter(subject=subject[0])
        #t =t.filter(subject=sub)
        totalAttendance=daily_attendance.objects.all().filter(teacher = t[0]).count()
        print(totalAttendance)
        present = 0
        a =daily_attendance.objects.all().filter(teacher = t[0])
        for i in a:
            p=i.student.split(',')
            print(p)
            for k in p:
                if str(s.roll_no)==k:
                    present=present+1
        print(present)
    return render(request, 'students/totalAttendance.html',{'s':s,'sub':sub, 'totalAttendance':totalAttendance, 's':s,'present':present,'i':i})

@login_required
def monthlyAttendance(request):
    s=get_object_or_404(Student,user=request.user)
    c=s.class_info
    t =Teacher.objects.all().filter(class_info=c)
    sub = []
    for i in t:
        sub.append(i.subject)
    i=None
    m= None
    monthlyAttendance=0
    present =0
    if request.method == 'POST':
        i=request.POST.get('subject')
        m=request.POST.get('month')
        l=m.split('-')
        print(l)
        subject=Subject.objects.all().filter(subject=i)
        #d = request.POST.get('date')
        t=Teacher.objects.all().filter(class_info=c).filter(subject=subject[0])
        #t =t.filter(subject=sub)
        monthlyAttendance=daily_attendance.objects.all().filter(teacher = t[0]).filter(attendance_date__year=l[0] , attendance_date__month=l[1]).count()
        print(monthlyAttendance)
        present = 0
        a =daily_attendance.objects.all().filter(teacher = t[0]).filter(attendance_date__year=l[0] , attendance_date__month=l[1])
        for j in a:
            p=j.student.split(',')
            print(p)
            for k in p:
                if str(s.roll_no)==k:
                    present=present+1
        print(present)
    return render(request, 'students/monthlyAttendance.html',{'s':s,'sub':sub, 'monthlyAttendance':monthlyAttendance, 's':s,'present':present,'i':i, 'm':m})


@login_required
def yearlyAttendance(request):
    s=get_object_or_404(Student,user=request.user)
    c=s.class_info
    t =Teacher.objects.all().filter(class_info=c)
    sub = []
    for i in t:
        sub.append(i.subject)
    i=None
    y=0
    yearlyAttendance=0
    present =0
    if request.method == 'POST':
        i=request.POST.get('subject')
        y=request.POST.get('year')
        subject=Subject.objects.all().filter(subject=i)
        #d = request.POST.get('date')
        t=Teacher.objects.all().filter(class_info=c).filter(subject=subject[0])
        #t =t.filter(subject=sub)
        yearlyAttendance=daily_attendance.objects.all().filter(teacher = t[0]).filter(attendance_date__year= y).count()
        print(yearlyAttendance)
        present = 0
        a =daily_attendance.objects.all().filter(teacher = t[0]).filter(attendance_date__year=y)
        for j in a:
            p=j.student.split(',')
            print(p)
            for k in p:
                if str(s.roll_no)==k:
                    present=present+1
        print(present)
    return render(request, 'students/yearlyAttendance.html',{'s':s,'sub':sub, 'yearlyAttendance':yearlyAttendance, 's':s,'present':present,'i':i, 'y':y})
@login_required
def viewAttendance(request):
    s=get_object_or_404(Student,user=request.user)
    return render(request,'students/viewAttendance.html',{'s':s})
@login_required
def Listofsubject(request):
    s=get_object_or_404(Student,user=request.user)
    c=s.class_info
    t =Teacher.objects.all().filter(class_info=c)
    sub = []
    for i in t:
        sub.append(i.subject)
    return render(request,'students/Listofsubject.html',{'s':s,'sub':sub,'t':t})

def viewAssignment(request):
    s=Student.objects.get(user=request.user)
    t=Teacher.objects.all().filter(class_info=s.class_info)
    a=Assignment.objects.all().filter(class_info=s.class_info)
    return render(request,'students/Listofassignment.html',{'s':s,'t':t,'a':a})
