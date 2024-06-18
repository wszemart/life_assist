from django.contrib import admin

from .models import Book, BookAuthor, Movie

admin.site.register(BookAuthor)
admin.site.register(Book)
admin.site.register(Movie)
