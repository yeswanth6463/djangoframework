from django.shortcuts import render
from regstrapp.forms import userProfileForm,UserForm



# Create your views here.
def register(request):
    registered=False
    if request.method=='POST':
         form1=userProfileForm(request.POST,request.FILES)
         form2=UserForm(request.POST)
         if form1.is_valid() and form2.is_valid():
            # print(form1.cleaned_data['address'])
            # print(form2.cleaned_data['username'])
            user=form2.save()
            user.set_password(user.password)
            user.save()
            
            profile = form1.save(commit=False)
            profile.user=user #connecting default user model with userprofile model
            profile.save()
            registered=True
    else:
            form1=userProfileForm()
            form2=UserForm()
    context={
        'form1':form1,
        'form2':form2,
        'registered':registered
    }
    return render(request,'registration.html',context)
    
