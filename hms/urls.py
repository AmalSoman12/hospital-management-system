from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('og-admin/', admin.site.urls),
    path('hospital/', include('hospital.urls')),
    path('admin/', include('customadmin.urls')),
]