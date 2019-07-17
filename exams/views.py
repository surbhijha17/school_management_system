from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from teachers.models import Teacher
from students.models import Student

#from PayTm import Checksum
#def Exams(request):
#    e = Examname.objects.all()
#    return render(request, 'exams/allsub.html',{'e':e})
@login_required
def Exams(request):
    s=get_object_or_404(Student,user=request.user)
    c=s.class_info
    t =Teacher.objects.all().filter(class_info=c)
    e = []
    for i in t:
        e.append(i.subject)
    return render(request, 'exams/allsub.html',{'s':s,'e':e})
@login_required
def Topics(request,examname):
    sub=Subject.objects.get(subject=examname)
    s=get_object_or_404(Student,user=request.user)
    e=Topic.objects.filter(examname=sub,classname=s.class_info)
    return render(request,'exams/alltopic.html',{'s':s,'sub':sub,'e':e})

@login_required
def level(request,examname,tname):
    s=get_object_or_404(Student,user=request.user)
    to=Topic.objects.get(tname=tname)

    l=Level.objects.all().filter(topic=to)
    if request.method=="POST":
        a = request.POST.get("submit")
        t=Level.objects.get(topic=to,lname=a)
        #if t.value==1:
        return redirect('exams:StartTest',examname=examname,tname=tname,value=t.value)
        #else:
        #    return redirect('exams:Checkout',pk=t.pk)
    return render(request,'exams/level.html',{'s':s,'l':l})

#@login_required
def starttest(request,examname,tname,value):
    s=get_object_or_404(Student,user=request.user)
    sub=Subject.objects.get(subject=examname)
    v=Topic.objects.get(examname=sub,tname=tname)
    r=Level.objects.get(topic=v,value=value)
    
    q=Questions.objects.all().filter(level = r)
    c=Questions.objects.all().filter(level = r).count()
    #c=Questions.objects.all().filter(level = r).count()
    #q=Questions.objects.all().filter(level = r)
    if request.method=="POST":
        return redirect('exams:Ques',examname=examname,tname=tname,value=r.value)
    return render(request,'exams/start.html',{'s':s,'r':r,'c':c,'q':q})


@login_required
def question(request,examname,tname,value):
    s=get_object_or_404(Student,user=request.user)
    sub=Subject.objects.get(subject=examname)
    v=Topic.objects.get(examname=sub,tname=tname)
    r=Level.objects.get(topic=v,value=value)
    q=Questions.objects.all().filter(level = r)
    c=Questions.objects.all().filter(level = r).count()
    pos=0
    neg=0
    x=[]
    y=[]
    result=0
    a=r.timeslot

    #print(rank)
    #countTrack.objects.all().delete()
    if request.method=="POST":
        lv=Level.objects.get(pk =r.pk)
        cou=countTrack.objects.filter(user=request.user,level=lv).count()
        if cou==0:
            countTrack.objects.create(user=request.user,level=lv,counter=1,flag=False)
        else:
            b=countTrack.objects.filter(user=request.user,level=lv)
            m=b[0].counter+1
            b.update(counter=m,flag=False)

        for i in q:
            y.append(i.ans)
            p=request.POST.get(str(i.id))
            if(p==None):
                p="None"
            x.append(p)
            v=zip(q,x,y)

        total=0

        for j,i in zip(q,range(0,c)):
            #print(x[i])#user answer
            #print(y[i])#correct answer

            if x[i]=="None":
                pass
            elif x[i]==y[i]:
                pos+=j.PMarks
            else:
                neg+=j.NMarks

            #print(pos)
            #print(neg)
            result= pos-neg
            total+=j.PMarks
            n=Result.objects.filter(user=request.user,level=lv).count()
            if n==0:
                Result.objects.create(user=request.user,score=result,level=lv)
            else:
                Result.objects.filter(user=request.user,level=lv).update(score=result)
        rank=Result.objects.all().filter(level=r).order_by('-score')
        temp=[]
        for i in rank:
            temp.append(i.user)
        u=request.user
        index=temp.index(u)
        index=index+1

        return render(request,'exams/showresult.html',{'s':s,'x':x,'y':y,'result':result,'c':c,'v':v, 'total':total,'index':index})
    return render(request, 'exams/ques.html', {'s':s,'q':q,'a':a})
