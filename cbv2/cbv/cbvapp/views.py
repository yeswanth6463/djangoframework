from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView,DeleteView
from django.http import HttpResponse
from cbvapp.models import Company, Product
from django.urls import reverse_lazy

# Create your views here.
class htmlPageView(TemplateView):
    template_name = 'index.html'

class AllCompaniesList(ListView):
    model = Company
    context_object_name = 'Companylist'

class CompanyDetails(DetailView):
    model = Company
    context_object_name = 'company_details'

class Addcompany(CreateView):
    model = Company
    fields = '__all__'

class UpdateCompany(UpdateView):
    model = Company
    fields = ['name', 'ceo', 'logo']

# EMI Calculation Logic
def calculate_emi(principal, annual_interest_rate, tenure_years):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    tenure_months = tenure_years * 12
    
    if monthly_interest_rate == 0:
        emi = principal / tenure_months
    else:
        emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure_months) / \
              ((1 + monthly_interest_rate) ** tenure_months - 1)
    
    return round(emi, 2)

def emi_calculator(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    emi = None
    error_message = None
    
    if request.method == 'POST':
        try:
            loan_amount = float(request.POST.get('loan_amount'))
            annual_interest_rate = float(request.POST.get('interest_rate'))
            tenure_years = int(request.POST.get('tenure'))
            
            if loan_amount <= 0 or annual_interest_rate < 0 or tenure_years <= 0:
                error_message = "Please enter valid positive values for all fields."
            else:
                emi = calculate_emi(loan_amount, annual_interest_rate, tenure_years)

        except ValueError:
            error_message = "Invalid input. Please enter numeric values."
    
    context = {
        'product': product,
        'emi': emi,
        'error_message': error_message
    }
    return render(request, 'cbvapp/emi_calculator.html', context)


class DeleteCompany(DeleteView):
    model=Company
    success_url=reverse_lazy('list')