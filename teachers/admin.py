from django.contrib import admin
from .models import Teacher, Assignment
# Register your models here.

class TeacherTable(admin.ModelAdmin):
	model=Teacher
	list_display=('name','subject','classes')

	def name(self,obj):
		return obj.user.first_name
	def classes(self,obj):
		classes=[]
		string=""
		for c in obj.class_info.all():
			classes.append(c)
		for c in classes:
			string=string+c.name+","
		return string

admin.site.register(Teacher,TeacherTable)
admin.site.register(Assignment)
