from django.db import models
from django.utils import six, timezone
from datetime import *
from django.contrib.auth.models import User
from model_utils.fields import StatusField
from model_utils import Choices
from classes.models import ClassInfo,Subject
from teachers.models import Teacher
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

#class Attendance(models.Model):
#	prof=models.ForeignKey(Teacher,on_delete=models.CASCADE)
#	student=models.ForeignKey(Student,on_delete=models.CASCADE)
#	total_att=models.IntegerField(default=0,null=True)
#	day = models.DateTimeField()
#	is_present = models.BooleanField(default = False)
#	def __str__(self):
#		return "attendance of professor name: " + str(self.prof)+" of subject  " +str(self.prof.subject) +" of  roll no " +str(self.student.roll_no) +" of class "+str(self.student.class_info)


class daily_attendance(models.Model):
	student = models.CharField(max_length = 500)
	class_info = models.ForeignKey(ClassInfo, on_delete=models.CASCADE, default=0)
	teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
	attendance_date = models.DateField( default=date.today)
	update_date = models.DateTimeField('update_date', default=datetime.now)
	mark = models.BooleanField(default=False)
	def __str__(self):
		return str(self.attendance_date)
