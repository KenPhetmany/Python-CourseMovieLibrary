from django.contrib import admin
from .models import Genre, Movie  # Importing the classes

# How the adminstration area will manage the movies, the user interface


# List to customize how we work with genres in the admin  ui. ModelAdmin contains functions we can use
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # What to display on the ui


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )  # Excludes certain fields
    list_display = ('title', 'number_in_stock', 'release_year', 'id')


admin.site.register(Genre, GenreAdmin)  # Registers the models for the ui
admin.site.register(Movie, MovieAdmin)
