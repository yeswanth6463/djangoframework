from django.shortcuts import render,redirect
from defectsportal.models import Defectsprofile,Defects_screen_shots
from defectsportal.forms import Defect_Edit_Form,AddDefectForm

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
    print(f"Number of images: {img.count()}")
    context = {

        'desc':desc,
        'img':img
    }
    
    
    return render(request,"defects/desc.html",{'context':context})

@login_required(login_url='login')
def add_defect(request):
    items = AddDefectForm()
    if request.method == 'POST':
        items = AddDefectForm(request.POST)
        if items.is_valid():
            items.save()
            return redirect('defect')
    return render(request, 'defects/add_defects.html', {'items': items})

@login_required(login_url='login')
def edit(request,id=0):
    defect = Defectsprofile.objects.get(id=id)
    form = Defect_Edit_Form(instance=defect)
    if request.method == 'POST':
        form = Defect_Edit_Form(request.POST, instance=defect)
        if form.is_valid():
            form.save()
            return redirect('defect')
    return render(request, 'defects/edit_defects.html', {'form': form})


@login_required(login_url='login')
def delete_defects(request, id=0):
    defect = Defectsprofile.objects.get(id=id)
    defect.delete()
    return redirect('defect')