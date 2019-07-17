from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import  UserAdmin
from .forms import *
from .models import CustomUser
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render,redirect
User=get_user_model()
class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email','first_name')
    actions=['send_email']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    def send_email(self, request, queryset):
        form = SendEmailForm(initial={'users': queryset})
        return render(request, 'accounts/send_email.html', {'form': form})
    send_email.short_description = "Send an email to selected users"

admin.site.register(User, CustomUserAdmin)
