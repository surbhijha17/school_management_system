from django.db import models
from attendance.models import *


class Registeration(models.Model):
    name = models.CharField(max_length =20)
    cls = models.ForeignKey(ClassInfo, on_delete = models.CASCADE)
    dob = models.DateField()
    father = models.CharField(max_length=20)
    mother = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    add = models.CharField(max_length=100)

    def __str__(self):
        return self.email
