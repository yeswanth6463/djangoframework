from django.shortcuts import render,redirect
from defectsportal.models import Defectsprofile,Defects_screen_shots
from defectsportal.forms import Defect_Edit_Form,AddDefectForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def alldefects(request):
    defects=Defectsprofile.objects.all()
    total_defects=len(defects)
    
    return render(request,"defects/defects.html",{'defects':defects,'total_defects':total_defects})

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
            return redirect('defects')  # Redirect to the main defects list
    return render(request, 'defects/add_defects.html', {'items': items})

@login_required(login_url='login')
def edit(request,id=0):
    defect = Defectsprofile.objects.get(id=id)
    form = Defect_Edit_Form(instance=defect)
    if request.method == 'POST':
        form = Defect_Edit_Form(request.POST, instance=defect)
        if form.is_valid():
            form.save()
            return redirect('defects')  # Redirect to the main defects list
    return render(request, 'defects/edit_defects.html', {'form': form})

@login_required(login_url='login')
def delete_defects(request, id=0):
    try:
        defect = Defectsprofile.objects.get(id=id)
        defect.delete()
        messages.success(request, 'Defect deleted successfully.')
    except Defectsprofile.DoesNotExist:
        messages.error(request, 'Defect not found.')
    return redirect('defects')  # Redirect to the main defects list
@login_required(login_url='login')
def add_defects(request,id=0):
    defect = Defectsprofile.objects.get(id=id)
    form = AddDefectForm()
    if request.method == 'POST':
        form = AddDefectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('defects')  # Redirect to the main defects list
        return render(request, 'defects/add_defects.html',{'form':form,'defect':defect})
    
    