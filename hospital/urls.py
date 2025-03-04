
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('appoinment', views.book_appoinment,name='book_appoinment'),
    path('appoinment_temp', views.appoinment,name='appoinment'),    
    path('get_doctors/', views.get_doctors, name='get_doctors'),
    path('token/<int:token_id>/', views.token, name='token'),
    path('services/', views.services, name='services'),
    path('department/',views.department, name='department'),
    path('doctors/',views.doctors, name='doctors'),
    path('contacts/',views.contacts, name='contacts'),
    path('about/',views.about, name='about'),
    path('login/',views.login_user, name='login_user'),
    path('signup/',views.signup_user, name='signup_user'),
    path('logout/',views.logout_user, name='logout_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)