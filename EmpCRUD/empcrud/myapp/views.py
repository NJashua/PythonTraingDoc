from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Employee
from .forms import DepartmentForm, EmployeeForm
from django.views.decorators.csrf import csrf_exempt

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    employees = Employee.objects.filter(department=department)
    return render(request, 'department_detail.html', {'department': department, 'employees': employees})

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department_form.html', {'form': form})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'department_confirm_delete.html', {'department': department})

def employee_create(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.department = department
            employee.save()
            return redirect('department_detail', pk=pk)
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form, 'department': department})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('department_detail', pk=employee.department.pk)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form, 'department': employee.department})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        department_pk = employee.department.pk
        employee.delete()
        return redirect('department_detail', pk=department_pk)
    return render(request, 'employee_confirm_delete.html', {'employee': employee})

def employee_search(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        try:
            employee = Employee.objects.select_related('department').get(pk=emp_id)
            return render(request, 'employee_detail.html', {'employee': employee})
        except Employee.DoesNotExist:
            error_message = f"Employee with ID {emp_id} does not exist."
            return render(request, 'employee_search.html', {'error_message': error_message})
    return render(request, 'employee_search.html')
