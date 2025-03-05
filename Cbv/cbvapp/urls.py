from django.urls import path
from cbvapp import views

urlpatterns = [
    
    path('',views.AllcompaniesList.as_view()),
    path('<int:pk>/',views.CompanyDetails.as_view())
    
    ]