from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from cbvapp.models import Company,Product
import math
from django.urls import reverse_lazy


# Create your views here.
# class myclassView(View):
#     def get(self,request):
#         return HttpResponse('<h1>This is Class Based View</h1>')

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
    fields = ['name','ceo','logo']
    
class DeleteCompany(DeleteView):
    model = Company
    success_url = reverse_lazy('list')
    
    
class EMICalculatorView(View):
    template_name = 'cbvapp/emi_calculator.html'

    def get(self, request):
        """Display the EMI calculator form with initial values from query parameters."""
        product_name = request.GET.get('product_name', '')
        product_price = request.GET.get('price', '')

        context = {
            'product_name': product_name,
            'product_price': product_price
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """Process EMI calculation after form submission."""
        product_name = request.POST.get('product_name', '')
        product_price = request.POST.get('product_price', '')
        loan_amount = request.POST.get('loan_amount', '')
        interest_rate = request.POST.get('interest_rate', '')
        tenure = request.POST.get('tenure', '')

        # Validate input values
        try:
            product_price = float(product_price)
            loan_amount = float(loan_amount)
            interest_rate = float(interest_rate)
            tenure = int(tenure)

            if loan_amount > product_price:
                return render(request, self.template_name, {
                    'error': "Loan amount cannot exceed product price!",
                    'product_name': product_name,
                    'product_price': product_price
                })

            # EMI Formula Calculation
            monthly_interest_rate = (interest_rate / 100) / 12
            tenure_months = tenure * 12

            if monthly_interest_rate > 0:
                emi = (loan_amount * monthly_interest_rate * math.pow(1 + monthly_interest_rate, tenure_months)) / \
                      (math.pow(1 + monthly_interest_rate, tenure_months) - 1)
            else:
                emi = loan_amount / tenure_months  # No interest case

            return render(request, self.template_name, {
                'product_name': product_name,
                'product_price': product_price,
                'loan_amount': loan_amount,
                'interest_rate': interest_rate,
                'tenure': tenure,
                'emi': round(emi, 2)
            })

        except ValueError:
            return render(request, self.template_name, {
                'error': "Invalid input! Please enter valid numbers.",
                'product_name': product_name,
                'product_price': product_price
            })
