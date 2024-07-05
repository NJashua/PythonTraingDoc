from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from testapp.models import Company

class CompanyListView(ListView):
    model = Company
    template_name = 'testapp/company_list.html'
    context_object_name = 'company_list'

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'testapp/company_detail.html'
    context_object_name = 'company'

class CompanyCreateView(CreateView):
    model = Company
    fields = ('name', 'location', 'ceo')
    template_name = 'testapp/company_form.html'

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('name', 'location', 'ceo')
    template_name = 'testapp/company_form.html'
    success_url = reverse_lazy('companies')

class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'testapp/company_confirm_delete.html'
    success_url = reverse_lazy('companies')
