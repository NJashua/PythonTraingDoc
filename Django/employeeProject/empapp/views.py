from django.shortcuts import render
from .models import Employee

def display_employee(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'display_employee.html', context)
