from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('slogin/', views.slogin, name='slogin'),
    path('student-register/', views.student_register, name='student_register'),
]
