from django.shortcuts import render
from userapp.forms import MediaForm
from userapp.models import UserMedia


# Create your views here.

def index(request):
    form = MediaForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }

    return render(request,'index.html',context)    

def display(request):
    data = UserMedia.objects.all()
    context = {
        'data':data
    }
    return render(request,"display.html",context)

def profile(request):
    return render(request,'profile.html')

def about(request):
    return render(request,'about.html')

def footer(request):
    return render(request,'footer.html')