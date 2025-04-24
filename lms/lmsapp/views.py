from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm

def slogin(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        if not user_type:
            error_message = "Please select a user type."
        else:
            # Placeholder validation logic based on user_type
            if user_type == 'student':
                if username == 'studentuser' and password == 'studentpass':
                    return redirect('student_dashboard')  # Replace with actual student dashboard URL name
                else:
                    error_message = "Invalid student credentials."
            elif user_type == 'teacher':
                if username == 'teacheruser' and password == 'teacherpass':
                    return redirect('teacher_dashboard')  # Replace with actual teacher dashboard URL name
                else:
                    error_message = "Invalid teacher credentials."
            elif user_type == 'admin':
                if username == 'adminuser' and password == 'adminpass':
                    return redirect('admin_dashboard')  # Replace with actual admin dashboard URL name
                else:
                    error_message = "Invalid admin credentials."
            else:
                error_message = "Invalid user type selected."

    return render(request, 'slogin.html', {'error_message': error_message})

def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login or another page after successful registration
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_register.html', {'form': form})
