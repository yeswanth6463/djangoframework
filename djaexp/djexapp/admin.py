from django.contrib import admin
from django.urls import path
from djexapp.models import * 
# Register your models here.
admin.site.register(user_name)
admin.site.register(user_profile)
