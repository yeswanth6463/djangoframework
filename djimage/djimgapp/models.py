from django.db import models

# Create your models here.
class usermidea(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    upload_time=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='userimg/',blank=True,null=True)