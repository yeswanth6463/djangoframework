from django import forms
from django.contrib.auth.models import user

class UserProfileForm(forms.modelForm):
    class meta:
        model=user
        fields=[
            "username",
            "email",
            "password"
        ]
