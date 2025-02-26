from django.shortcuts import render,redirect
from defectsportal.models import Defectsprofile,Defects_screen_shots

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def alldefects(request):
    defects=Defectsprofile.objects.all()
    return render(request,"defects/defects.html",{'defects':defects})

@login_required(login_url='login')
def desc(request, id=0):
    desc=Defectsprofile.objects.get(id=id)
    img=Defects_screen_shots.objects.filter(defect=desc)
    context={
        'desc':desc,
        'img':img
    }
    
    
    return render(request,"defects/desc.html",{'context':context})