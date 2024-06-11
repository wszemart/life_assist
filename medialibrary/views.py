from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book, Movie
from .forms import BookForm


class BookListView(ListView):
    model = Book
    template_name = 'medialibrary/book_list_v2.html'
    context_object_name = 'books'


class BookCreateView(CreateView):
    model = Book
    template_name = 'medialibrary/book_form.html'
    form_class = BookForm
    success_url = reverse_lazy("medialibrary:book-list")


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'medialibrary/book_form.html'
    form_class = BookForm
    success_url = reverse_lazy("medialibrary:book-list")
    context_object_name = 'book'


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("medialibrary:book-list")


class MovieListView(ListView):
    model = Movie
    template_name = 'medialibrary/movie_list.html'
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'medialibrary/movie_detail.html'
    context_object_name = 'movie'
