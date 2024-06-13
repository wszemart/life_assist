from django.db import models


class Book(models.Model):
    RATING_CHOICES = [
        ("Terrible", "Terrible"),
        ("Bad", "Bad"),
        ("Okay", "Okay"),
        ("Really good!", "Really good!"),
        ("New favorite!", "New favorite!"),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    rating = models.CharField(null=True, blank=True, max_length=100, choices=RATING_CHOICES)

    def __str__(self):
        return self.title


class Movie(models.Model):
    RATING_CHOICES = [
        ("Terrible", "Terrible"),
        ("Bad", "Bad"),
        ("Okay", "Okay"),
        ("Really good!", "Really good!"),
        ("New favorite!", "New favorite!"),
    ]

    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    rating = models.CharField(max_length=100, choices=RATING_CHOICES, null=True, blank=True)
