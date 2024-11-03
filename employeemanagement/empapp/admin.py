from django.contrib import admin
from .models import Company, Project, Employee

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'company')
    search_fields = ('name',)
    list_filter = ('company',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'company')
    search_fields = ('name', 'email')
    list_filter = ('company',)