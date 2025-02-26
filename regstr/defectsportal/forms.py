from defectsportal.models import Defectsprofile
from django import forms

class defectsform(forms.ModelForm):
    class Meta:
        model=Defectsprofile
        fields=['defects_id',
                'defect_name',
                'defect_type',
                'assigned_by',
                'assigned_to',
                'description',
                'priority'
                ]
        
class AddDefectForm(forms.ModelForm):
    class Meta:
        model = Defectsprofile
        fields='__all__'
        

class Defect_Edit_Form(forms.ModelForm):
    class Meta:
        model = Defectsprofile
        
    