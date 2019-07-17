from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from students.models import Student
from classes.models import ClassInfo
from django.contrib.auth.decorators import login_required
from django.conf import settings
from Paytm import Checksum
from django.template.loader import render_to_string
#MERCHANT_KEY = 'R0W22FOsG7hhQOY%'
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from django.contrib.auth.decorators import user_passes_test

def check_student(user):
    return user.student_set.exists()

def acess(request):
    return render(request,'fee/error.html')
MERCHANT_KEY = 'R0W22FOsG7hhQOY%'
def GeneratePdf(request,pk):
        f=Fee.objects.get(pk=pk)
        c=f.student.class_info
        if f.amount == float(f.student.class_info.monthlyfees)+float(f.student.class_info.admissionfees)+float(f.student.class_info.ExtraFees):
            admissionfees=c.admissionfees
            monthlyfees=c.monthlyfees
            extrafees=c.ExtraFees
        else:
            admissionfees=0
            monthlyfees=c.monthlyfees
            extrafees=c.ExtraFees
        pdf = render_to_pdf('fee/invoice.html', {'f':f,'admissionfees':admissionfees,'monthlyfees':monthlyfees,'extrafees':extrafees})

        return HttpResponse(pdf, content_type='application/pdf')

@login_required
@user_passes_test(check_student,login_url='/fee/error/',redirect_field_name=None)
def fee(request):
    student=Student.objects.get(user=request.user)
    c=ClassInfo.objects.get(name=student.class_info.name)
    admissionfees=0
    monthlyfees=0
    extrafees=0
    if Fee.objects.filter(student=student,paymentstatus="successful").count()==0:
        admissionfees=c.admissionfees
        monthlyfees=c.monthlyfees
        extrafees=c.ExtraFees
    else:
        admissionfees=0
        monthlyfees=c.monthlyfees
        extrafees=c.ExtraFees
    totalfees=float(monthlyfees)+float(admissionfees)+float(extrafees)




    id=None
    if request.method=="POST":
        i=Fee.objects.create(student=student,amount=totalfees)


        # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {
                'MID': 'SGijGB62559210222772',
                'ORDER_ID':"school"+str(i.orderid),
                'TXN_AMOUNT': str(i.amount),
                'CUST_ID': request.user.email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/fee/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'fee/paytm.html', {'param_dict': param_dict})
    return render(request, 'fee/payment.html',{ 'student':student,'totalfees':totalfees,'admissionfees':admissionfees,'monthlyfees':monthlyfees,'extrafees':extrafees})

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    pk=None
    f=None
    t=None
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        print(response_dict['RESPCODE'])
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            i=response_dict['ORDERID']
            print(i)
            t=i[6:]
            Fee.objects.filter(orderid=t).update(paymentstatus='success')

        else:
            print('order was not successful because' + response_dict['RESPMSG'])
        i=response_dict['ORDERID']
        t=i[6:]
        f=Fee.objects.get(orderid=t)
        print(f.pk)
    return render(request, 'fee/paymentstatus.html', {'response_dict': response_dict,'f':f})
