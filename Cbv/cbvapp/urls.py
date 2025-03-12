from django.urls import path, include

from cbvapp import views

urlpatterns = [
    path('company/', views.AllcompaniesList.as_view(), name='company_list'),

    
    path('',views.AllcompaniesList.as_view()),
path('<int:pk>/', views.CompanyDetails.as_view(), name='company'),
    path('addcompany/', views.Createcompany.as_view(), name='company_form'),
    path('edit/<int:pk>/',views.Updatecompany.as_view(),name='edit'),
    # path('emi/<int:pk>/',views.)
    path('emi/<int:pk>/',views.emi_cals,name='emi'),



    
    ]
