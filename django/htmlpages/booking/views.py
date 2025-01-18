from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'booking/index.html')
def booking_history(request):
    return render(request,'booking/booking_history.html')
def detail(request):
    return render(request,'booking/detail.html')
