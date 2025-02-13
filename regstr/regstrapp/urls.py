from django.urls import path
from regstrapp import views

urlpatterns=[
    path("",views.register)
]