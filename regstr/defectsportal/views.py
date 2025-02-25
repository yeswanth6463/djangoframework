from django.shortcuts import render
from defectsportal.models import Defectsprofile


# Create your views here.

def alldefects(request):
    defects=Defectsprofile.objects.all()
    return render(request,"defects/defects.html",{'defects':defects})

def desc(request,id=0):
    desc=Defectsprofile.objects.get(id=0)
    return render(request,"defects/desc.html",{'desc':desc})