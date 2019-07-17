from django.db import models

#from students.models import Student
# Create your models here.

class Subject(models.Model):
	subject=models.CharField(max_length=10)
	def __str__(self):
		return self.subject

class ClassInfo(models.Model):
	name =models.CharField(max_length=10)
	admissionfees = models.CharField(max_length=4)
	monthlyfees = models.CharField(max_length=4)
	ExtraFees =models.CharField(max_length=3)
	strength = models.CharField(max_length=2)
	def __str__(self):
		return self.name
