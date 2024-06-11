from bootstrap_datepicker_plus.widgets import YearPickerInput
from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField(required=True)
    author = forms.CharField(required=True)
    summary = forms.CharField(widget=forms.Textarea)
    published_date = YearPickerInput()
    rating = forms.IntegerField(required=True)

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
