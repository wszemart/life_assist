from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    summary = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    summary = models.TextField()
    rating = models.IntegerField(default=0)

