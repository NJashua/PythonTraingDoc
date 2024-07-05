from django.shortcuts import render, redirect
from testapp.forms import EmployeeForm
from testapp.models import Employee
from django.http import HttpResponse

def show_view(request):
    employees = Employee.objects.all()
    filter_data = {}
    if len(employees)<0:
            filter_data = {"Remark" : "No Employee data is there to represent"}
    
    return render(request, 'index.html', {'employees': employees, "filter_key":filter_data})


def get_table_data(request):
    data_val = "James Bond"
    emp_data = Employee.objects.all()
    return HttpResponse(request, content=data_val)

def insert_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'insert.html', {'form': form})

def delete_view(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'update.html', {'employee': employee})
 

# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from testapp.models import Employee
# from testapp.forms import EmployeeForm
# from django.http import HttpResponse
# from django import template

# register = template.Library()

# @register.filter
# def add_dollar(value):
#     return f'${value}'


# class EmployeeListView(ListView):
#     model = Employee
#     template_name = 'index.html'
#     context_object_name = 'employees'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if context['employees'].count() == 0:
#             context['filter_key'] = {"Remark": "No Employee data is there to represent"}
#         return context

# class TableDataView(DetailView):
#     model = Employee

#     def get_object(self, queryset=None):
#         return HttpResponse("James Bond")

# class EmployeeCreateView(CreateView):
#     model = Employee
#     form_class = EmployeeForm
#     template_name = 'insert.html'
#     success_url = reverse_lazy('employee-list')

# class EmployeeUpdateView(UpdateView):
#     model = Employee
#     form_class = EmployeeForm
#     template_name = 'update.html'
#     success_url = reverse_lazy('employee-list')

# class EmployeeDeleteView(DeleteView):
#     model = Employee
#     success_url = reverse_lazy('employee-list')
