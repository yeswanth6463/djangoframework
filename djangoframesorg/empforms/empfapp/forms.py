from django import forms 

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    age  = forms.IntegerField()
    phone  = forms.IntegerField()
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    address = forms.CharField(max_length=250)
    

    def clean_name(self):
        name = self.cleaned_data['name']
        if ord(name[0]) >= 45 and ord(name[0]) <=57:
            raise forms.ValidationError('Name should not startswith numbers')
        return name

    def clean_age(self):
        age = self.cleaned_data['age']
        if age <= 0:
            raise forms.ValidationError('Age must be positive value and above 0')
        return age

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(str(phone)) !=10:
            raise forms.ValidationError('phone number should contains 10 digits ')
        return phone

    # def clean_confirm_password(self):
    #     password = self.cleaned_data['password']
    #     confirm_password = self.cleaned_data['confirm_password']
    #     if password !=  confirm_password:
    #         raise forms.ValidationError('This password is unmatching')
    #     return confirm_password

    def clean(self):
        cleaned_data = super().clean()
        
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password !=  confirm_password:
            raise forms.ValidationError('This password is unmatching')
        return confirm_password