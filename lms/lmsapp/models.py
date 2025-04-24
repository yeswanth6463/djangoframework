from django.db import models
from django.contrib.auth.models import User 
import datetime
import os

# Create your models here.
  
class Student(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    username=models.CharField(max_length=500)
    profile_img=models.ImageField(upload_to='student_profile_imgs/',null=True)

    def __str__(self) :
        return self.fullname

    def enrolled_courses(self):
        enrolled_courses=StudentCourseEnrollment.objects.filter(student=self).count()
        return enrolled_courses

    def favorite_courses(self):
        favorite_courses=StudentFavoriteCourse.objects.filter(student=self).count()
        return favorite_courses

    def complete_assignments(self):
        complete_assignments=StudentAssignment.objects.filter(student=self,student_status=True).count()
        return complete_assignments

    def pending_assignments(self):
        pending_assignments=StudentAssignment.objects.filter(student=self,student_status=False).count()
        return pending_assignments

    class Meta:
        verbose_name_plural="5. Students"



