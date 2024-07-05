from django import forms
from .models import Department, Employee

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'dept_location']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_name', 'emp_salary', 'emp_email', 'department']
