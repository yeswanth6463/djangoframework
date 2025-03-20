from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from rest_framework import status

from .models import Category, Product
# Create your views here.

class ProductList(APIView):
    def get(self, request, category_slug=None):
        category = None
        products = Product.objects.filter(available=True)
        categories = Category.objects.all()
        
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        
        return Response({
            'category': category,
            'products': products,
            'categories': categories,
        })

    category =None
    products = Product.objects.filter(available=True)
    categories  =Category.object.all()
    
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 'products/product/list.html',{
        'category': category,
        'products': products,
        'categories':categories,
    })
    
class ProductDetail(APIView):
    def get(self, request, id, slug):
    product= get_object_or_404(Product, id=id, slug=slug, available=True )
    return render(request,'products/product/detail.html',
                  {'product': product})
