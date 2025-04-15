from django.shortcuts import render ,redirect ,HttpResponse
from django.http import JsonResponse
from . models import Category,Product,Cart,favorite
from .form import CustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json

# Create your views here.

def home(request):
    product=Product.objects.filter(trending=True)
    return render(request,'shop/index.html',{'product':product})

def logout_page(request):
    
    
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect('/')

def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      #print(request.user.id)
      product_status=Product.objects.get(id=product_id)
      if product_status:
          if Cart.objects.filter(user=request.user.id,product_id=product_id):
              return JsonResponse({'status':' Already  added in  Cart'}, status=200)
          else:
              if product_status.quantity>=product_qty:
                  Cart.objects.create(
                      user=request.user,
                      product_id=product_id,
                      product_quantity=product_qty
                  )
                  return JsonResponse({'status':' Added in  Cart'}, status=200)
              else:
                  return JsonResponse({'status':'Stock not availabel '}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Cart'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)

def fav_view(request):
    if request.user.is_authenticated:
        fav_items = favorite.objects.filter(user=request.user)
        return render(request, 'shop/fav.html', {'fav_items': fav_items})
    else:
        messages.error(request,'Login to access Favourite')
        return redirect('/login')

def fav_remove(request,fid):
    favitem=favorite.objects.get(id=fid)
    favitem.delete()
    return redirect('/favview')

def cart_page(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).select_related('product')
        for item in cart:
            item.total = item.product.selling_price * item.product_quantity
        return render(request, 'shop/cart.html', {'cart': cart})
    else:
        messages.error(request,'Login to access Cart')
        return redirect('/login')

def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect('/cart')

def fav(request):
    if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status':'Invalid Access'}, status=400)
    
    if not request.user.is_authenticated:
        return JsonResponse({'status':'Login to Add Favourite'}, status=401)

    try:
        data = json.loads(request.body)
        product_id = data['pid']
        product_status = Product.objects.get(id=product_id)
        
        if favorite.objects.filter(user=request.user.id, product_id=product_id).exists():
            return JsonResponse({'status':'Already added to Favourites'}, status=200)
        else:
            favorite.objects.create(
                user=request.user,
                product_id=product_id,
            )
            return JsonResponse({'status':'Added to Favourites'}, status=200)
            
    except json.JSONDecodeError:
        return JsonResponse({'status':'Invalid JSON data'}, status=400)
    except KeyError:
        return JsonResponse({'status':'Missing product ID'}, status=400)
    except Product.DoesNotExist:
        return JsonResponse({'status':'Product not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status':f'Error: {str(e)}'}, status=500)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
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