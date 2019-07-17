from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import date
from classes.models import Subject, ClassInfo
User = get_user_model()
# Create your models here.

class Topic(models.Model):
    tname = models.CharField(max_length=20)
    classname = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
    examname = models.ForeignKey(Subject, on_delete = models.CASCADE)

    def __str__(self):
        return self.tname

class Level(models.Model):
    lname = models.CharField(max_length=20)
    value=models.IntegerField()
    topic = models.ForeignKey('Topic', on_delete= models.CASCADE)
    Amount=models.IntegerField()
    timeslot=models.IntegerField(default='60')
    def __str__(self):
        return str(self.topic)+" " + str(self.lname)


class Questions(models.Model):
    level = models.ForeignKey('Level', on_delete=models.CASCADE)
    ques = models.TextField()
    quesadditionalpart = RichTextUploadingField(blank=True)
    opt1 = models.CharField(max_length=100)
    opt2 = models.CharField(max_length=100)
    opt3 = models.CharField(max_length=100)
    opt4 = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)
    PMarks = models.IntegerField(default=4)
    NMarks = models.IntegerField(default=1)
    solution=RichTextUploadingField(blank=True)
    def __str__(self):
        return self.ques


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score=models.IntegerField()
    level=models.ForeignKey(Level,on_delete=models.CASCADE)
    date=models.DateField(default=date.today())

    def __str__(self):
        return  str(self.user.email)+" - "+str(self.score)

class countTrack(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    level=models.ForeignKey(Level,on_delete=models.CASCADE)
    counter=models.IntegerField(default=0)
    flag=models.BooleanField(default=False)

    def __str__(self):
        return str(self.counter)

class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    level=models.ForeignKey(Level,on_delete=models.CASCADE)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.EmailField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    paymentstatus = models.CharField(max_length=100,default="Unsuccessful")

    def __str__(self):
        return "order-id "+str(self.order_id)+" -  "+str(self.paymentstatus)
