from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login'),
    path('collections/',views.collections,name='collections'),

    path('collections/<str:name>/',views.collectionsView ,name='collections'),
    path('collections/<str:cname>/<str:pname>/',views.product_details ,name='product_details'),



    
]
