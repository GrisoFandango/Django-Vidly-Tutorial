from django.db import models
from django.utils import timezone

# Create your models here.

# Inside models we can create classes to put in the DB


class Genre(models.Model):
    # Charfield indicate that need to be a string, and we can set the lenght for security purpose
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    # IntegerField indicate that that field has to be an integer
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    # Here the same for the Float
    daily_rate = models.FloatField()
    # ForeignKey it is used to create correlation between different classes
    # in this case we link the genre to the other data of the movie
    # on_delete describe the behaviour in case the genre category is delete. Cascade cancel all the entries with that genre in this case
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.title
