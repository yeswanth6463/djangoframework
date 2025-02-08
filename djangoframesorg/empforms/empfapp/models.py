from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age  = models.IntegerField()
    phone  = models.BigIntegerField()
    address = models.CharField(max_length=250)