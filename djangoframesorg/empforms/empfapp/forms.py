from django import forms 
from empfapp.models import Employee

class EmployeeForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    # age = forms.IntegerField()
    # phone = forms.IntegerField()
    # password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    # confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    # address = forms.CharField(max_length=250)

    class Meta:
        model = Employee
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data['name']
        if ord(name[0]) >= 45 and ord(name[0]) <= 57:
            raise forms.ValidationError('Name should not start with numbers')
        return name

    # def clean_age(self):
    #     age = self.cleaned_data['age']
    #     if age <= 0:
    #         raise forms.ValidationError('Age must be a positive value above 0')
    #     return age

    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']
    #     if len(str(phone)) != 10:
    #         raise forms.ValidationError('Phone number should contain 10 digits')
    #     return phone

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm_password')

    #     if password and confirm_password and password != confirm_password:
    #         raise forms.ValidationError('Passwords do not match')
        
    #     return cleaned_data
