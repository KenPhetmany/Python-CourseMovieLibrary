from django.urls import path
from . import views

# movies/
# movies/1/details

app_name = 'movies'
urlpatterns = [  # List of objects that map url endpoints
    # Specifying the endpoint. This the root of app.
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
