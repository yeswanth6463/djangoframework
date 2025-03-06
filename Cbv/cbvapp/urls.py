from django.urls import path, include

from cbvapp import views

urlpatterns = [
    path('company/', views.AllcompaniesList.as_view(), name='company_list'),

    
    path('',views.AllcompaniesList.as_view()),
path('<int:pk>/', views.CompanyDetails.as_view(), name='company'),


    
    ]
