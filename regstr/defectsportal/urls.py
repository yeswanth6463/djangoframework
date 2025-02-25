from django.urls import path
from . import views

urlpatterns = [
    path('', views.alldefects, name='defects'),
    path('desc/<int:id>',views.desc, name='desc')
    # Add your other URL patterns here
]
