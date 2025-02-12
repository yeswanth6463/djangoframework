from django.urls import path
from regstrapp import views

urlspatterns=[
    path("",views.register)
]