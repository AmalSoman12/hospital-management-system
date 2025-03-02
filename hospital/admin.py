from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Department)

class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('name','department','photo')
admin.site.register(Doctors,DoctorsAdmin)


class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ('status','token_number','department','doctor','date','first_name','last_name','phone','message')
admin.site.register(Appoinment,AppoinmentAdmin)




