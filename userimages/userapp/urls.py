from django.urls import path
from userapp import views

urlpatterns = [
   path('',views.index,name="index"),
    path('display/',views.display,name="display"),
    path('profile/',views.profile,name="profile"),
    path('about/',views.about,name="about"),
   
]