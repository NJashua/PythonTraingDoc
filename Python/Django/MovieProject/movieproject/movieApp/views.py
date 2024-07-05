# movieApp/views.py

from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

def index_view(request):
    return render(request, 'index.html')

def add_movie_view(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'addmovie.html', {'form': form})

def list_movie_view(request):
    movies_list = Movie.objects.all().order_by('-rating')
    return render(request, 'listmovie.html', {'movies_list': movies_list})
