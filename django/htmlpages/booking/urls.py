from django.urls import path
from booking import views

urlpatterns = [
    path('',views.index),
    path('detail',views.detail),
    path('booking_history',views.booking_history)
]