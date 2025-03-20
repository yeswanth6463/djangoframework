from django.urls import path
from apiapp import views


urlpatterns =[
    path('',views.userapi,name='userapi'),
    path('countryapi',views.countryapi,name='countryapi'),
    path('trainapi',views.Trainapidata,name='trainapi'),
    path('trainapi/<int:id>',views.Trainapidata,name='trainapi'),
    path('savefile',views.saveFile,name='savefile')
    ]