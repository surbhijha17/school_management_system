from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from attendance.models import *
from .forms import *
# Create your views here.

def inquiry(request):

    c=ClassInfo.objects.all()
    p=None
    if request.method == 'POST':
        t=request.POST.get('class_info')
        p=get_object_or_404(ClassInfo, name=t)

    return render(request,'admission/inquiry.html',{'c':c,'p':p})

def Registeration(request):
    form1 = RegisterationForm()
    form2 = SignupForm()
    if request.method == 'POST':
        form1=RegisterationForm(request.POST or None)
        form2=SignupForm(request.POST or None)
        if form1.is_valid() and form2.is_valid():
            a=form1.save(commit=False)
            user=form2.save(commit=False)

            user.is_active=False
            a.email=user.email
            user.save()
            a.save()

    return render(request, 'admission/registeration.html', {'form1':form1, 'form2':form2})
