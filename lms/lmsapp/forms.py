from django.contrib.auth.forms import UserCreationForm
from .models import User, Student
from django import forms
from django.core.exceptions import ValidationError


class Studentform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }


class StudentRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = Student
        fields = ['fullname', 'email', 'username', 'profile_img']
        widgets = {
            'profile_img': forms.ClearableFileInput(),
        }
        labels = {
            'fullname': 'Full Name',
            'email': 'Email',
            'username': 'Username',
            'profile_img': 'Profile Picture',
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        student = super().save(commit=False)
        student.password = self.cleaned_data["password1"]  # In real app, hash password properly
        if commit:
            student.save()
        return student
