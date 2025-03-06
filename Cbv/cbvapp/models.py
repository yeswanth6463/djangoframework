from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class company(models.Model):
    cmp_name=models.CharField(max_length=100)
    cmp_ceo=models.CharField(max_length=100)
    origin=models.CharField(max_length=100)
    image = models.ImageField(upload_to='userimg/',blank=True,null=True)

    def __str__(self):
        return self.cmp_name
    
class product(models.Model):
    cmp=models.ForeignKey(company,related_name='company', on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_color=models.CharField(max_length=100)
    fuletype=models.CharField(max_length=100)
    seatcapasity=models.IntegerField()
    
    def __str__(self):
        return self.product_name
    
