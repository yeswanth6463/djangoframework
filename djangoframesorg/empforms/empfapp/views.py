from django.shortcuts import render
from empfapp.forms import EmployeeForm

# Create your views here.
def index(request):
    form=EmployeeForm()
    return render(request,'index.html',{'form':form})

