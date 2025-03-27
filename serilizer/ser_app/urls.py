from django.urls import path
from . import views

urlpatterns = [
    path('',views.serapp, name="api"),
    path('apilist/',views.taskList, name="apilist"),
    path('Detail/<str:pk>',views.taskDetail,name='Detail'),
    path('Create/',views.taskCreate,name='Create'),
    path('Update/<str:pk>',views.taskUpdate,name='Update'),
    path('delete/<str:pk>',views.taskdelete,name="delete")
]
