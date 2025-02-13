from django.shortcuts import render
from regstrapp.forms import UserProfileForm


# Create your views here.
def register(request):
    form=UserProfileForm()
    context={
        'form':form
    }
    return render(request,'registration.html',context)
    
