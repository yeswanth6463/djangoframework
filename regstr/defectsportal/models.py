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




# Create your models here.
class Defectsprofile(models.Model):
    
    defect_id=models.CharField(max_length=100)
    defect_name=models.CharField(max_length=100)
    defect_type=models.CharField(max_length=100,choices=DEFECTS_TYPES,default='PRIMARY')
    assigned_by=models.CharField(max_length=100)
    assigned_to=models.CharField(max_length=100)
    description=models.TextField()
    priority=models.CharField(max_length=100,choices=DEFECTS_PRIORITY,default='HIGH')
    
def __str__(self):
    return self.defect_name
