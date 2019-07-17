from django.db import models
from students.models import Student
from datetime import date

class Fee(models.Model):
	orderid=models.AutoField(primary_key=True)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	amount = models.IntegerField( default=0)
	paidupto = models.CharField(max_length=50,blank=True)
	paymentdate = models.DateField(default=date.today())
	paymentstatus = models.CharField(max_length=100,default="Unsuccessful")
