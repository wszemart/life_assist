from django.urls import path

from medialibrary.views.author.create import BookAuthorCreateView
from medialibrary.views.author.delete import BookAuthorDeleteView
from medialibrary.views.author.detail import BookAuthorDetailView
from medialibrary.views.author.update import BookAuthorUpdateView
from medialibrary.views.book.create import BookCreateView
from medialibrary.views.book.delete import BookDeleteView
from medialibrary.views.book.detail import BookDetailView
from medialibrary.views.book.list import BookListView
from medialibrary.views.book.update import BookUpdateView
from medialibrary.views.mainpage import MedialibraryMainPage
from medialibrary.views.movie.create import MovieCreateView
from medialibrary.views.movie.delete import MovieDeleteView
from medialibrary.views.movie.detail import MovieDetailView
from medialibrary.views.movie.list import MovieListView
from medialibrary.views.movie.update import MovieUpdateView

app_name = "medialibrary"

urlpatterns = [
    path("", MedialibraryMainPage.as_view(), name="medialibrary"),
    path("authors/new/", BookAuthorCreateView.as_view(), name="create-author"),
    path("authors/<int:pk>/update", BookAuthorUpdateView.as_view(), name="author-update"),
    path("authors/<int:pk>/", BookAuthorDetailView.as_view(), name="author-detail"),
    path("authors/<int:pk>/delete/", BookAuthorDeleteView.as_view(), name="author-delete"),
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
