from django.db import models
from django.urls import reverse
from django.shortcuts import redirect


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    ceo = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='userimg/',blank=True,null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail",kwargs={"pk": self.pk})

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    seat_capacity = models.IntegerField()
    price = models.IntegerField()
    Company = models.ForeignKey(Company,related_name='companies',on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    
class ProductImages(models.Model):
    products = models.ForeignKey(Product,related_name='products',on_delete=models.CASCADE)
    product_img = models.ImageField(upload_to='productimg/',blank=True,null=True)


def my_view(request):
    return redirect(reverse('emi'))    


    