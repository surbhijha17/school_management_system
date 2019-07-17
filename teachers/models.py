from django.db import models
from django.contrib.auth import get_user_model
from classes.models import ClassInfo,Subject
User=get_user_model()
from datetime import date
# Create your models here.

class Teacher(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	class_info=models.ManyToManyField(ClassInfo,blank=True)
	subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
	photo=models.ImageField(null=True,upload_to='media/',blank=True)

	class Meta:
		permissions = (("is_teacher", "is_teacher"), )

	def __str__(self):
		return self.user.first_name

def upload(instance,filename):
	new_filename='{} Assignment.{}'.format(instance.teacher.subject,filename.split('.')[-1])
	return "teachers/{}/assignment/{}/{}".format(instance.teacher.user.first_name,instance.class_info.name,new_filename)
class Assignment(models.Model):
	teacher=models.ForeignKey('Teacher', on_delete=models.CASCADE)
	file = models.FileField(null=True, upload_to=upload,blank=True)
	class_info = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
	duedate = models.DateField(default=date.today())

	def __str__(self):
		return str(self.teacher.user.first_name)+" "+str(self.class_info)
