from django import forms
from djimgapp.models import usermidea

class MediaForm(forms.ModelForm):
    class Meta:
        model=usermidea
        fields='__all__'