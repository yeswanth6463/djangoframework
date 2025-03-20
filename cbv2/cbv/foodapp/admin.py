from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Category,Recipe,Fooditem 


# Register your models here.
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Fooditem)