from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    #additional field
    phone=models.BigIntegerField()
    address=models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    image=models.ImageField(upload_to='userimage/',blank=True)
    
    def __str__(self):
        return self.user.username