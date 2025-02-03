from django import forms

class EmployeeForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    phone=forms.IntegerField()
    address=forms.CharField(max_length=250)
    