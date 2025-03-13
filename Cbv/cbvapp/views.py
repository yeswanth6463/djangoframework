from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView
from django.http import HttpResponse
from cbvapp.models import company,product,productimages

# Create your views here.
class htmlview(TemplateView):
    template_name = 'index.html'

class AllcompaniesList(ListView):
    model = company
    context_object_name = 'company_list'

class CompanyDetails(DetailView):
    model = company
    context_object_name = 'company_details'

class Createcompany(CreateView):
    model = company
    fields = '__all__'
    queryset = company.objects.all()  # Define the queryset

class Updatecompany(UpdateView):
    model = company 
    fields = ['cmp_name','cmp_ceo','image']

def emi_cals(request, pk):  # Accept pk as an argument
    product_instance = product.objects.get(id=pk)  # Fetch the product by ID
    user_data = request.user  # Get user data

    if request.method == 'POST':
        try:
            loan_amount = float(request.POST.get('loan_amount'))
            total_tenure = int(request.POST.get('total_tenure'))
            interest_rate = float(request.POST.get('interest_rate'))
        except ValueError:
            return render(request, 'emi.html', {
                'product': product_instance,
                'user': user_data,
                'error_message': 'Please enter valid numeric values for loan amount, total tenure, and interest rate.'
            })

        
        # Validate loan amount against product price
        product_price = product_instance.product_price
        if loan_amount > product_price:
            return render(request, 'emi.html', {
                'product': product_instance,
                'user': user_data,
                'error_message': 'Loan amount cannot exceed the product price.'
            })

        # Perform calculations here (e.g., EMI calculation)
        r = interest_rate / 12 / 100  # Convert annual interest rate to monthly and percentage
        n = total_tenure * 12
        emi_amount = loan_amount * r * (1 + r) ** n / ((1 + r) ** n - 1)
    
        # Pass the values to the template
        return render(request, 'emi.html', {
            'product': product_instance,
            'user': user_data,
            'loan_amount': loan_amount,
            'total_tenure': total_tenure,
            'interest_rate': interest_rate,
            'emi_amount': emi_amount
        })
        
    return render(request, 'emi.html', {'product': product_instance, 'user': user_data})
