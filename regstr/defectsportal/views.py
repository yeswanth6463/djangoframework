from django.shortcuts import render
from defectsportal.models import Defectsprofile


# Create your views here.
def alldefects(request):
    defects=Defectsprofile.objects.all()
    return render(request,"defects/defects.html",{'defects':defects})