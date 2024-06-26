from bootstrap_datepicker_plus.widgets import YearPickerInput
from django import forms

from .models import Book, BookAuthor, Movie


class BookAuthorForm(forms.ModelForm):
    class Meta:
        model = BookAuthor
        fields = [
            "name",
            "surname",
        ]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "published_date",
            "summary",
            "rating",
        ]
        widgets = {"published_date": YearPickerInput()}


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            "title",
            "director",
            "release_date",
            "summary",
            "rating",
        ]
        widgets = {"release_date": YearPickerInput()}
