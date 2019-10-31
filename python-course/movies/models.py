from django.db import models
from django.utils import timezone

# Classes that represent the domain of the app. E.g. classes of
# movies will have title, genre, release year


class Genre(models.Model):  # Model contains the functions.
    name = models.CharField(max_length=225)  # Set a fieldclass

    def __str__(self):  # Specify the genre class with a property, in this case Name
        return self.name


class Movie(models.Model):  # new class
    title = models.CharField(max_length=225)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    # Creates a relationship betweeen the Genre and Movie class
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
