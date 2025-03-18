
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from hospital.models import *  
from django.contrib.auth.models import User

def sidebar(request):
    return render(request, 'sidebar.html')



def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)  # For debugging purposes

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Check if the user is a superuser
            if user.is_superuser:
                login(request, user)
                return redirect('user_list')  # Redirect to the admin dashboard or sidebar
            else:
                messages.error(request, 'You do not have permission to access this page.')
        else:
            messages.error(request, 'Invalid credentials')

        return render(request, 'admin_login.html')  # Render the login page with error messages

    return render(request, 'admin_login.html')  # Render the login page for GET requests

def doctors_list(request):
    doctors = Doctors.objects.all()
    context = {
        'doctors': doctors
    }
    return render(request, 'doctors_list.html',context)

def department_list(request):
    departments = Department.objects.all()
    context = {
        'departments': departments
    }
    return render(request, 'department_list.html',context)

def appoinment_list(request):
    departments = Department.objects.all()
    doctors = Doctors.objects.all()
    appoinments = Appoinment.objects.all()
    context = {
        'appoinments': appoinments,
        'departments': departments,
        'doctors': doctors
    }   
    return render(request, 'appoinment_list.html',context)

def user_list(request):
    users = User.objects.filter(is_superuser=True)
    context = {
        'users': users
    }
    return render(request, 'user_list.html',context)

def logout_admin(request):
    logout(request)
    return redirect('admin_login')