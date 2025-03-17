from django.urls import path
from cbvapp import views
from cbvapp.views import EMICalculatorView
urlpatterns = [
    path('',views.AllCompaniesList.as_view(),name='list'),
    path('<int:pk>/',views.CompanyDetails.as_view(),name='detail'),
    path('create',views.Addcompany.as_view(),name='create'),
    path('edit/<int:pk>/',views.UpdateCompany.as_view(),name='edit'),
    path('delete/<int:pk>/',views.DeleteCompany.as_view(),name='delete'),
    path('company/emi-calculator/', EMICalculatorView.as_view(), name='emi_calculator')
]