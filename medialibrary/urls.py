from django.urls import path

from .views import (
    BookCreateView,
    BookDeleteView,
    BookDetailView,
    BookListView,
    BookUpdateView,
    MedialibraryMainPage,
    MovieCreateView,
    MovieDeleteView,
    MovieDetailView,
    MovieListView,
    MovieUpdateView,
)

app_name = "medialibrary"

urlpatterns = [
    path("", MedialibraryMainPage.as_view(), name="medialibrary"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/new/", BookCreateView.as_view(), name="create-book"),
    path("books/<int:pk>/update", BookUpdateView.as_view(), name="book-update"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies/new/", MovieCreateView.as_view(), name="create-movie"),
    path("movies/<int:pk>/update", MovieUpdateView.as_view(), name="movie-update"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("movies/<int:pk>/delete/", MovieDeleteView.as_view(), name="movie-delete"),
]
