from django.contrib import admin
from .models import Student,Teacher,Admin
from django.contrib.auth.models import User, Group
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Admin)