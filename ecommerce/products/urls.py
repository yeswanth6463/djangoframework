from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.Product_list., name='product_list'),
    path('<slug')
]