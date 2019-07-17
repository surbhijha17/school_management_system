from django.contrib import admin

from .models import daily_attendance
# Register your models here.

class DailyAtnd(admin.ModelAdmin):
	model=daily_attendance
	list_display=('attendance_date','teacher','class_info','sub')

	def sub(self,obj):
		return obj.teacher.subject

admin.site.register(daily_attendance,DailyAtnd)
