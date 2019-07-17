from django.http import HttpResponse
from django.shortcuts import render

#def homepage(request):
##	return render(request,"attenhome.html",{'student':student})
def home(request):
    return render(request,'index.html')

def about(request):
	return render(request,'about.html')
def curriculum(request):
	return render(request,'curriculum.html')