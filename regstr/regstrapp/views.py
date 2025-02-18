from django.shortcuts import render, redirect
from regstrapp.forms import userProfileForm,UserForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


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

def user_login(request):
    if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
      
      #authentication 
       user = authenticate(username=username, password=password)
       if user:
              if user.is_active:
                  login(request,user)
                  return redirect('home')
              else:
                  return HttpResponse('user is not active')
       else:
              return HttpResponse('pls check ur creds')
    return render(request,'login.html')

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashbord.html')
    
