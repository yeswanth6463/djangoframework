from django.shortcuts import render
import requests
from django.http import JsonResponse


# Create your views here.
def userapi(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    user=response.json()
    
    return render(request,'userapi.html',{'user':user})

def countryapi(request):
    response = requests.get('https://restcountries.com/v3.1/all')
    country = response.json()
    
    return render(request , 'countryapi.html',{'country':country})

