from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def contact(request):
    return render(request, 'contact.html')
def carrer(request):
    return render(request, 'carrer.html')
