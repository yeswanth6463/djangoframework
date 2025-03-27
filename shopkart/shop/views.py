from django.shortcuts import render ,redirect
from . models import Category,Product
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'shop/index.html')

def register(request):
    return render(request, 'shop/register.html')

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
