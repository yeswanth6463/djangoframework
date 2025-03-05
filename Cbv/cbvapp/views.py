from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from cbvapp.models import company,product

# Create your views here.
class htmlview(TemplateView):
    template_name = 'index.html'

# class myclassview(view):
#     def get(self, request):
#         return HttpResponse("<h1> hello welcome to the cbv </h1> ")

class AllcompaniesList(ListView):
    model = company
    # context_object_name='allcompanies'
    #company_list

class CompanyDetails(DetailView):
    model = company
    context_object_name='company_details'
    
    