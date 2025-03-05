from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminlogin,name='admin_login'),
    path('sidebar/',views.sidebar, name='sidebar'),
    path('doctors_list/',views.doctors_list, name='doctors_list'),
    path('department_list/',views.department_list, name='department_list'),
    path('appoinment_list/',views.appoinment_list, name='appoinment_list'),
    path('user_list/',views.user_list, name='user_list'),
    path('logout_admin/',views.logout_admin, name='logout_admin'),
]
