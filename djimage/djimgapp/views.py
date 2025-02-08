from django.shortcuts import render
from djimgapp.forms import MediaForm
from djimgapp.models import usermidea

# Create your views here.

def index(request):
    form=MediaForm()
    if request.method=='POST':
        form = MediaForm(request.POST,request.FILES)
        if form.is_valid():
           form.save()
    context ={
        'form':form
    }
    return render(request,"index.html",context)
def display(request):
    data=usermidea.objects.all()
    context={
        'data':data
    }
    return render(request,'display.html',context)



#  
