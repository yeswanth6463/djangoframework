from defectsportal.models import Defectsprofile
from django import forms

class defectsform(forms.ModelForm):
    class Meta:
        model=Defectsprofile
        fields=['defect_id',
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
    defect_id=forms.CharField(max_length=100,disabled=True)
    
    defect_type=forms.CharField(disabled=True)
    class Meta:
        model = Defectsprofile
        fields='__all__'
        
        
    