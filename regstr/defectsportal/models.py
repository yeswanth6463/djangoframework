from django.db import models

DEFECTS_TYPES = [
    ('PRIMARY','primary'),
    ('SECONDARY','secondary'),
    ('TERTIARY','tertiary'),
]

DEFECTS_PRIORITY=[
    ('HIGH','high'),
    ('MEDIUM','medium'),
    ('LOW','low'),
]

DEFECTS_STATUS=[
    ('COMPLETED','completed'),
    ('NOT COMPLETED','not completed')
]




# Create your models here.
class Defectsprofile(models.Model):
    
    defect_id=models.CharField(max_length=100)
    defect_name=models.CharField(max_length=100)
    defect_type=models.CharField(max_length=100,choices=DEFECTS_TYPES,default='PRIMARY')
    assigned_by=models.CharField(max_length=100)
    assigned_to=models.CharField(max_length=100)
    description=models.TextField()
    priority=models.CharField(max_length=100,choices=DEFECTS_PRIORITY,default='HIGH')
    status=models.CharField(max_length=100,choices=DEFECTS_STATUS,default='COMPLETED')
    
    def __str__(self):
        return self.defect_name

class Defects_screen_shots(models.Model):
    defect=models.ForeignKey(Defectsprofile,related_name='defect',on_delete=models.CASCADE)
    defect_image = models.ImageField(
        upload_to='defectsimg/',blank=True,null=True
    )
    
    

