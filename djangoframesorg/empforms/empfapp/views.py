from django.shortcuts import render
from empfapp.forms import EmployeeForm

# Create your views here.
def index(request):
    form = EmployeeForm()

    if request.method =='POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            print('validation success')

            print(form.cleaned_data['name'])
            print(form.cleaned_data['age'])
            print(form.cleaned_data['phone'])
            print(form.cleaned_data['address'])

    return render(request,'index.html',{'form':form})