from django import forms
from userapp.models import UserMedia

class MediaForm(forms.ModelForm):
    class Meta:
        model = UserMedia
        fields = '__all__'