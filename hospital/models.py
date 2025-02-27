from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctors(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.department})"
    
class Appoinment(models.Model):
    STATUS_CHOICES = [
        ('visited','Visited'),
        ('not visited', 'Not Visited') 
    ]
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='not visited')
    token_number = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    date = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True)
    
   

    def __str__(self):
        return f"Token {self.token_number} - {self.first_name} {self.last_name} - {self.doctor.name} ({self.department}) ({self.date}) ({self.status})"