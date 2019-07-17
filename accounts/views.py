from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import *
from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.http import HttpResponseRedirect,HttpResponse ,JsonResponse
from attendance import *
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model
from students.models import Student
from teachers.models import Teacher

User = get_user_model()
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.email, password=raw_password)

            login(request, user)
            return redirect('admission:inquiry')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
def login_view(request):
    if request.method =='POST':
        #form=AuthenticationForm(data=request.POST)
        #if form.is_valid():
        username= request.POST.get('email')

        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
               
        #user=form.get_user()
        

            if'next'in request.POST:
                return redirect(request.POST.get('next'))
            else:
                if Teacher.objects.filter(user=user).exists():
                    return redirect('teachers:profile')
                elif Student.objects.filter(user=user).exists():
                    return redirect('students:students_profile')
                else:
                    return redirect('admission:inquiry')
        else:
            
            messages.info(request,'Invalid Email or Password')     
    #else:
    #    form= AuthenticationForm()
    return render(request,'accounts/login.html',)
    #return render(request, 'templates/base.html')

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('accounts:login')

class SendUserEmails(FormView):
    template_name = 'accounts/send_email.html'
    form_class = SendEmailForm
    success_url = reverse_lazy('admin:accounts_customuser_changelist')

    def form_valid(self, form):
        users = form.cleaned_data['users']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        print(users)
        t=[]
        for u in users:
            t.append(str(u.email))
        print(t)
        send_mail(subject, message, 'surbhijha1717@gmail.com', t, fail_silently=True,)
        user_message = '{0} users emailed successfully!'.format(len(t))
        messages.success(self.request, user_message)
        return super(SendUserEmails, self).form_valid(form)
