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
        loan_amount = request.POST.get('loan_amount')
        total_tenure = request.POST.get('total_tenure')
        interest_rate = request.POST.get('interest_rate')
        
        # Perform calculations here (e.g., EMI calculation)
        # For now, just pass the values to the template
        return render(request, 'emi.html', {
            'product': product_instance,
            'user': user_data,
            'loan_amount': loan_amount,
            'total_tenure': total_tenure,
            'interest_rate': interest_rate
        })
        

    return render(request, 'emi.html', {'product': product_instance, 'user': user_data})
