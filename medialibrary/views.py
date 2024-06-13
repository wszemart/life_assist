from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import BookForm, MovieForm
from .models import Book, Movie


class MedialibraryMainPage(View):
    template_name = "medialibrary/medialibrary_main_page.html"

    def get(self, request) -> redirect:
        return render(request, self.template_name)


class BookListView(ListView):
    model = Book
    template_name = "medialibrary/book_list.html"
    context_object_name = "books"


class BookCreateView(CreateView):
    model = Book
    template_name = "medialibrary/book_form.html"
    form_class = BookForm
    success_url = reverse_lazy("medialibrary:book-list")


class BookUpdateView(UpdateView):
    model = Book
    template_name = "medialibrary/book_form.html"
    form_class = BookForm
    success_url = reverse_lazy("medialibrary:book-list")
    context_object_name = "book"


class BookDetailView(DetailView):
    model = Book
    template_name = "medialibrary/book_detail.html"
    context_object_name = "book"


class BookDeleteView(DeleteView):
    model = Book
    template_name = "medialibrary/book_delete_confirm.html"
    success_url = reverse_lazy("medialibrary:book-list")
    context_object_name = "book"


class MovieListView(ListView):
    model = Movie
    template_name = "medialibrary/movie_list.html"
    context_object_name = "movies"


class MovieCreateView(CreateView):
    model = Movie
    template_name = "medialibrary/movie_form.html"
    form_class = MovieForm
    success_url = reverse_lazy("medialibrary:movie-list")


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = "medialibrary/movie_form.html"
    form_class = MovieForm
    success_url = reverse_lazy("medialibrary:movie-list")
    context_object_name = "movie"


class MovieDetailView(DetailView):
    model = Movie
    template_name = "medialibrary/movie_detail.html"
    context_object_name = "movie"


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "medialibrary/movie_delete_confirm.html"
    success_url = reverse_lazy("medialibrary:movie-list")
    context_object_name = "movie"
