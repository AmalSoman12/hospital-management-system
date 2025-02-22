

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('appoinment', views.book_appoinment,name='book_appoinment'),
    path('appoinment_temp', views.appoinment,name='appoinment'),    
    path('get_doctors/', views.get_doctors, name='get_doctors'),
    path('token/<int:token_id>/', views.token, name='token'),
    path('services/', views.services, name='services')


]
