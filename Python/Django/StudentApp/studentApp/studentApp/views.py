# studentApp/views.py

from django.shortcuts import render
from .forms import MyForm

from django.http import JsonResponse

def api_data_view(request):
    data = {
        'message': 'Hello from API!',
        'content': 'API data here',
    }
    return JsonResponse(data)


def input_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            return render(request, 'input.html', {
                'name': name,
                'email': email,
                'age': age,
            })
    else:
        form = MyForm()
    
    return render(request, 'input.html', {'form': form})
