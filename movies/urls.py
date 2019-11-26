from django.urls import path
from . import views  # using the dot we specify to import the module from this directory

app_name = "movies"
# movies/
# movies/1/details
# URL configuration
urlpatterns = [
    path("", views.index, name="index"),  # this is the root of the app
    path("<int:movie_id>", views.detail, name="detail"),
]
