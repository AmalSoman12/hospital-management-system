from django.shortcuts import render, redirect ,get_object_or_404
from .models import Department, Doctors, Appoinment
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required




def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    return render(request, 'login.html')

def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username is already taken')
            return render(request, 'signup.html')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.set_password(password)
        user.save()

        messages.info(request, 'Account created successfully')

        return redirect('login')
    return render(request, 'signup.html')

def logout_user(request):
    logout(request)
    return render(request, 'login.html')


def index(request):
    departments = Department.objects.all()
    doctors = Doctors.objects.all()
    return render(request, 'index.html' ,  {
        'departments': departments,
        'doctors': doctors
    })  
@login_required
def book_appoinment(request):
    departments = Department.objects.all()
    doctors = Doctors.objects.all()
    return render(request, 'appoinment.html' ,  {
        'departments': departments,
        'doctors': doctors
    })
@login_required
def appoinment(request):
    departments = Department.objects.all()
    doctors = Doctors.objects.all()

    if request.method == 'POST':

        department_id = request.POST.get('department')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        try:
            department = Department.objects.get(id=department_id)
            doctor = Doctors.objects.get(id=doctor_id)

            appointment = Appoinment.objects.create(
                department=department,
                doctor=doctor,
                date=date,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                message=message
            )


            return redirect('token', token_id=appointment.token_number)

        except (Department.DoesNotExist, Doctors.DoesNotExist) as e:
            error_message = f"Error: {e}"
            return render(request, 'appoinment_temp.html', {
                'departments': departments,
                'doctors': doctors,
                'error_message': error_message
            })

    return render(request, 'appoinment_temp.html', {
        'departments': departments,
        'doctors': doctors
    })

def get_doctors(request):
    department_id = request.GET.get('department_id')
    doctors = Doctors.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse({'doctors': list(doctors)})

def token(request, token_id):
    token = get_object_or_404(Appoinment, token_number=token_id)
    return render(request, 'token_no.html', {'token': token}) 

def services(request):
    return render(request, 'services.html')

def department(request):
    return render(request, 'departments.html')

def doctors(request):
    doc = Doctors.objects.all()
    return render(request, 'doctors.html',{'doc':doc})

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')

