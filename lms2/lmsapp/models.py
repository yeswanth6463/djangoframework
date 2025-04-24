from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to='userimage/', blank=True)
    user_type = models.CharField(max_length=50, default='student')

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to='userimage/', blank=True)
    user_type = models.CharField(max_length=50, default='teacher')

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to='userimage/', blank=True)
    user_type = models.CharField(max_length=50, default='admin')

    def __str__(self):
        return self.user.username
