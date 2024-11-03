from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)        
    address = models.TextField()                   
    location = models.CharField(max_length=100)     
    company_type = models.CharField(max_length=50)  
    established_date = models.DateField()  

    def _str_(self):
        return self.name 

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employees/images/', null=True, blank=True)  

    def __str__(self):
        return self.name
