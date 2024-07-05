# movies/views.py
from django.shortcuts import render
from.models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'ovies/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    shows = movie.show_set.all()
    return render(request, 'ovies/movie_detail.html', {'movie': movie, 'hows': shows})