from django.shortcuts import render, redirect ,get_object_or_404
from .models import Department, Doctors, Appoinment
from django.http import JsonResponse
def index(request):
    departments = Department.objects.all()
    doctors = Doctors.objects.all()
    return render(request, 'index.html' ,  {
        'departments': departments,
        'doctors': doctors
    })  

def book_appoinment(request):
    departments = Department.objects.all()
    doctors = Doctors.objects.all()
    return render(request, 'appoinment.html' ,  {
        'departments': departments,
        'doctors': doctors
    })

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
    return render(request, 'doctors.html')

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')
