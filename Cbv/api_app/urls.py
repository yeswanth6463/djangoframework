from django.urls import path
from . import views

urlpatterns = [
    path('',views.userapi,name='userapi'),
    path('countryapi',views.countryapi,name='countryapi'),
]