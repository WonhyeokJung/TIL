from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

def new(request):
    movie = Movie.objects.all()
    new_pk = len(movie) + 1
    context={
        'new_pk':new_pk,
    }
    return render(request, 'movies/new.html', context)

def create(request):
    movie = Movie()
    movie.title = request.GET.get('title')
    movie.overview = request.GET.get('overview')
    movie.poster_path = request.GET.get('poster_path')
    movie.save()
    if request.GET.get('aa'):
        return redirect('detail', pk=movie.pk)
    return redirect('index')

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie,
    }
    return render(request, 'movies/detail.html', context)
