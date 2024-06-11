from django.urls import path
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView,MovieListView, MovieDetailView

app_name = "medialibrary"

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path("books/create/", BookCreateView.as_view(), name="create-book"),
    path('books/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
]