from django.db import models

# Create your models here.
class product(models.Model):
    product_name=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    price=models.IntegerField()
    qnty=models.IntegerField()

    def __str__(self):
        return  self.product_name + " " +str(self.qnty)