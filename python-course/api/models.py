from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie


class MovieResource(ModelResource):  # How Api calles models
    class Meta:  # Inner class defines meta data about our movie resource
        # Attribute for getting all movies, just returns a query
        queryset = Movie.objects.all()
        resource_name = 'movies'  # Determines what our endpoint will look like
        excludes = ['date_created']
