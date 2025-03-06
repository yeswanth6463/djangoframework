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
    context_object_name = 'company_list'

    # context_object_name='allcompanies'
class CompanyDetails(DetailView):
    model = company
    context_object_name = 'company_details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = self.object.company.all()  # Fetch related products
        return context

    
    
    #how to get data from another model
