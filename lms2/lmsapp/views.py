from django.shortcuts import render,redirect
from .forms import StudentForm, StudentprofileForm
from .models import Student
from django.contrib.auth.models import User, Group
# Create your views here.


from django.contrib.auth import authenticate, login

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import Student

from .models import Student, Teacher, Admin
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

def index(request):
    return render(request, 'index.html')

def slogin(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        if not user_type:
            error_message = "Please select a user type."
        else:
            user_type_lower = user_type.lower()
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                try:
                    if user_type_lower == 'student':
                        profile = Student.objects.get(user=user)
                        login(request, user)
                        return redirect('student_dashboard')
                    elif user_type_lower == 'teacher':
                        profile = Teacher.objects.get(user=user)
                        login(request, user)
                        return redirect('teacher_dashboard')
                    elif user_type_lower == 'admin':
                        profile = Admin.objects.get(user=user)
                        login(request, user)
                        return redirect('admin_dashboard')
                    else:
                        error_message = "Invalid user type."
                except (Student.DoesNotExist, Teacher.DoesNotExist, Admin.DoesNotExist):
                    error_message = "User profile not found for the selected user type."
            else:
                error_message = "Invalid username or password or inactive user."

    return render(request, 'login.html', {'error_message': error_message})


def student_register(request):
    if request.method == 'POST':
        user_form = StudentForm(request.POST)
        profile_form = StudentprofileForm(request.POST, request.FILES)
        form1 = user_form
        form2 = profile_form
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            user_type = profile_form.cleaned_data.get('user_type').lower()
            if user_type == 'student':
                profile.save()
            elif user_type == 'teacher':
                from .models import Teacher
                teacher_profile = Teacher(
                    user=user,
                    phone=profile.phone,
                    address=profile.address,
                    city=profile.city,
                    state=profile.state,
                    zipcode=profile.zipcode,
                    image=profile.image,
                    user_type='teacher'
                )
                teacher_profile.save()
            elif user_type == 'admin':
                from .models import Admin
                admin_profile = Admin(
                    user=user,
                    phone=profile.phone,
                    address=profile.address,
                    city=profile.city,
                    state=profile.state,
                    zipcode=profile.zipcode,
                    image=profile.image,
                    user_type='admin'
                )
                admin_profile.save()
            else:
                profile.save()
            return render(request, 'register.html', {'form1': form1, 'form2': form2, 'success': True})
    else:
        form1 = StudentForm()
        form2 = StudentprofileForm()
    context = {
        'form1':form1,
        'form2':form2,
    }
    if 'success' in request.GET:
        context['success'] = True
    else:
        context['success'] = False
    # Render the template with the context
    return render(request, 'register.html', context)
    
    
def student_dashboard(request):
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
        return render(request, 'student_dashboard.html', {'student': student})
    else:
        return redirect('slogin')
    
def teacher_dashboard(request):
    if request.user.is_authenticated:
        teacher = Teacher.objects.get(user=request.user)
        return render(request, 'teacher_dashboard.html', {'teacher': teacher})
    else:
        return redirect('slogin')