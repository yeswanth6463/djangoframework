from django import forms
from django.contrib.auth.models import User
from .models import Student




class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=['username','email','password']

class StudentprofileForm(forms.ModelForm):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model=Student
        fields=['phone','address','city','state','zipcode','image','user_type']
    # captcha = ReCaptchaField()
