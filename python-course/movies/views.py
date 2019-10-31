from django.http import HttpResponse  # Return an HTTP Response
from django.shortcuts import render
from . models import Movie

# View functions takes cares of the requests (Json, Text, HTML, XML) and then returns a response
#


def index(request):  # Represents the main page of an app
    movies = Movie.objects.all()
    output = ', '.join([m.title for m in movies])   #
    return HttpResponse(output)  # Returns an HttpResponse Object, "output"
