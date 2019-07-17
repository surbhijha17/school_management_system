from django.db import models
from django.utils import six, timezone
from datetime import *
from model_utils.fields import StatusField
from model_utils import Choices
from django.contrib.auth import get_user_model
from classes.models import ClassInfo
User=get_user_model()

class GuardDetail(models.Model):
	father=models.CharField(max_length=20,blank=True)
	fmobile=models.CharField(max_length=10,blank=True)
	femail = models.EmailField(default="qaz@gmail.com")
	mother=models.CharField(max_length=20,blank=True)
	mmobile=models.CharField(max_length=10,blank=True)
	memail = models.EmailField(default="cbaaa@gmail.com")

	def __str__(self):
		return self.father

class Document(models.Model):
	name=models.CharField(max_length=100)
	document = models.FileField(upload_to='documents/')

	def __str__(self):
		return self.name


class Student(models.Model):
	STATUS =Choices('Male','Female',)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	roll_no=models.CharField(max_length=20)
	gender=StatusField(blank=True)
	mobile_no=models.CharField(max_length=10)
	dob=models.DateField(blank=True, null=True)
	guardian=models.ForeignKey('GuardDetail',on_delete=models.CASCADE,blank=True)
	address=models.TextField(blank=True)
	class_info=models.ForeignKey(ClassInfo,on_delete=models.CASCADE)
	photu = models.ImageField(null=True,upload_to='media/',blank=True)
	document = models.ManyToManyField('Document',blank=True)


	def __str__(self):
		return self.user.first_name
