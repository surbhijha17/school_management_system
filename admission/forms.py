
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib import admin
from .models import Registeration

from django.contrib.auth.forms import UserCreationForm
User=get_user_model()



class SignupForm(UserCreationForm):

    class Meta:
        model=User
        fields=('email','password1','password2',)

class RegisterationForm(forms.ModelForm):

    class Meta:
        model=Registeration
        fields=('name', 'cls', 'dob', 'father', 'mother', 'mobile', 'add')
