from django.urls import path
from . import views

urlpatterns = [
    path('', views.alldefects, name='defects'),
    # Add your other URL patterns here
]
