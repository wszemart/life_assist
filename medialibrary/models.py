from django.db import models


class BookAuthor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Book(models.Model):
    RATING_CHOICES = [
        ("Terrible", "Terrible"),
        ("Bad", "Bad"),
        ("Okay", "Okay"),
        ("Really good!", "Really good!"),
        ("New favorite!", "New favorite!"),
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(BookAuthor, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    published_date = models.DateField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    rating = models.CharField(null=True, blank=True, max_length=100, choices=RATING_CHOICES)
    tom = models.IntegerField(null=True, blank=True)
    series_name = models.CharField(max_length=200, null=True, blank=True)

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
