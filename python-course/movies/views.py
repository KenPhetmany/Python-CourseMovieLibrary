from django.http import HttpResponse, Http404  # Return an HTTP Response
from django.shortcuts import render, get_object_or_404
from . models import Movie

# View functions takes cares of the requests (Json, Text, HTML, XML) and then returns a response
#


def index(request):  # Represents the main page of an app
    movies = Movie.objects.all()  # SELECT * FROM movies_movie
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
