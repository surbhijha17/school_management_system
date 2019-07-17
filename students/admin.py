from django.contrib import admin
from .models import *
# Register your models here.
# Register your models here.



class StudentTable(admin.ModelAdmin):
	list_display=('name','roll_no','class_info','dob','gender','email')
	def name(self,obj):
		return obj.user.first_name
	def email(self,obj):
		return obj.user.email

admin.site.register(Student,StudentTable)
admin.site.register(GuardDetail)
admin.site.register(Document)
