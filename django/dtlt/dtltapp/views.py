from django.shortcuts import render

def index(request):
    context={
        'name':'deadpool',
        'cities':['chennai','vellore','hosur','krishnagiri','vaniyambadi'],
        'std_details':(
            {'name':'kratos','degree':'B Tech','stream':'IT','marks':85,'grade':'A'},
            {'name':'yesh','degree':'B Tech','stream':'IT','marks':75,'grade':'A'},
            {'name':'yeswanth','degree':'B Tech','stream':'IT','marks':65,'grade':'A'},
            {'name':'divagar','degree':'B Tech','stream':'IT','marks':55,'grade':'A'},
            {'name':'manu','degree':'B Tech','stream':'IT','marks':35,'grade':'A'},
            {'name':'jagadish','degree':'B Tech','stream':'IT','marks':95,'grade':'A'},
            {'name':'abilash','degree':'B Tech','stream':'IT','marks':77,'grade':'A'},
        )
    }
    return render(request, 'index.html', context)
