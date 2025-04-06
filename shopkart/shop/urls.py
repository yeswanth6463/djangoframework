from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('cart',views.cart_page,name='cart'),
    path('fav',views.fav,name='fav'),
    path('favview',views.fav_view,name='favview'),
    path('fav_remove/<str:fid>',views.fav_remove,name='fav_remove'),
    path('remove_cart/<str:cid>',views.remove_cart,name='remove_cart'),
    path('collections/',views.collections,name='collections'),
    path('collections/<str:name>/',views.collectionsView ,name='collections'),
    path('collections/<str:cname>/<str:pname>/',views.product_details ,name='product_details'),
  path('addtocart',views.add_to_cart,name="addtocart"),

     # Add trailing slash version



    
]
