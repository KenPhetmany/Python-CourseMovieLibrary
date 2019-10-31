from django.contrib import admin
from . models import Genre, Movie

# How the adminstration area will manage the movies


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'number_in_stock', 'release_year')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
