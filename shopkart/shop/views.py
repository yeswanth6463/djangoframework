from django.shortcuts import render ,redirect ,HttpResponse
from . models import Category,Product
from .form import CustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    product=Product.objects.filter(trending=True)
    return render(request,'shop/index.html',{'product':product})
    
    
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect('/')

def login_page(request):
      if request.user.is_authenticated:
          return redirect('/')
      else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.error(request, 'login successfully')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('login')
        
        return render(request,"shop/login.html")
    

def register(request):
    form=CustomerForm()
    if request.method=='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('/login')
    return render(request, 'shop/register.html', {'form':form})

def collections(request):
    catagory=Category.objects.filter(status=0)
    return render(request, 'shop/collections.html',{"catagory":catagory})

def collectionsView(request,name):
    if(Category.objects.filter(name=name,status=0)):
        product=Product.objects.filter(category__name=name)
        return render(request, 'shop/products/index.html',{'product':product,'category':name})
    else:
        messages.warning(request,"No such Catagory Found")
        return redirect('collections')

def product_details(request,cname,pname):
   if(Category.objects.filter(name=cname,status=0)):
       if(Product.objects.filter(name=pname,category__name=cname)):
           product=Product.objects.get(name=pname,category__name=cname)
           return render(request, 'shop/products/product_details.html',{'product':product})
       else:
           messages.warning(request,"No such Product Found")
           return redirect('collections')
   else:
       messages.warning(request,"No such Catagory Found")
       return redirect("collections")