from django.urls import path
from htmlpgsapp import views

urlpatterns = [
    path('', views.index),
    path('aboutus', views.aboutus),
    path('contact',views.contact),
    path('carrer',views.carrer)
]