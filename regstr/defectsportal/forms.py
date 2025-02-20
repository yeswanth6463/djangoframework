from defectsportal.models import Defectsprofile

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