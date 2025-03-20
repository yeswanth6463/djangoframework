from django.db import models

# Create your models here.
class Category(models.Model):
  
    category=models.CharField(max_length=100)
    origin=models.CharField(max_length=100)
    
    def __str__(self):
        return self.category
class Fooditem(models.Model):
      name=models.CharField(max_length=100)
      origin=models.CharField(max_length=100)
      def __str__(self):
            return self.name 
    
    
class Recipe(models.Model):

    item1=models.CharField(max_length=100)
    item2=models.CharField(max_length=100)
    item3=models.CharField(max_length=100)
    item4=models.CharField(max_length=100)
    item5=models.CharField(max_length=100)
    item6=models.CharField(max_length=100)
    item7=models.CharField(max_length=100)
    description=models.TextField()
