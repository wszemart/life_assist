# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
# from django.utils.functional import cached_property
# from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
# from view_breadcrumbs import BaseBreadcrumbMixin, CreateBreadcrumbMixin, DetailBreadcrumbMixin, ListBreadcrumbMixin
#
# from .forms import BookAuthorForm, BookForm, MovieForm
# from .models import Book, BookAuthor, Movie
#
#
# class MedialibraryMainPage(BaseBreadcrumbMixin, LoginRequiredMixin, TemplateView):
#     template_name = "medialibrary/medialibrary_main_page.html"
#
#     @cached_property
#     def crumbs(self):
#         breadcrumb_list = [
#             ("Dashboard", reverse_lazy("dashboard")),
#             ("Medialibrary", None),
#         ]
#         return breadcrumb_list


# class BookAuthorCreateView(CreateBreadcrumbMixin, LoginRequiredMixin, CreateView):
#     model = BookAuthor
#     template_name = "medialibrary/bookauthor_form.html"
#     form_class = BookAuthorForm
#     success_url = reverse_lazy("medialibrary:book-list")
#
#     @cached_property
#     def crumbs(self):
#         breadcrumb_list = [
#             ("Dashboard", reverse_lazy("dashboard")),
#             ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
#             ("Books", reverse_lazy("medialibrary:book-list")),
#             ("Create author", None),
#         ]
#         return breadcrumb_list


# class BookAuthorUpdateView(DetailBreadcrumbMixin, LoginRequiredMixin, UpdateView):
#     model = BookAuthor
#     template_name = "medialibrary/bookauthor_form.html"
#     form_class = BookAuthorForm
#     success_url = reverse_lazy("medialibrary:book-list")
#     context_object_name = "bookauthor"
#
#     @cached_property
#     def crumbs(self):
#         breadcrumb_list = [
#             ("Dashboard", reverse_lazy("dashboard")),
#             ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
#             ("Books", reverse_lazy("medialibrary:book-list")),
#             ("Update author", None),
#         ]
#         return breadcrumb_list


# class BookAuthorDetailView(DetailBreadcrumbMixin, LoginRequiredMixin, DetailView):
#     model = BookAuthor
#     template_name = "medialibrary/bookauthor_detail.html"
#     context_object_name = "bookauthor"
#
#     @cached_property
#     def crumbs(self):
#         breadcrumb_list = [
#             ("Dashboard", reverse_lazy("dashboard")),
#             ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
#             ("Books", reverse_lazy("medialibrary:book-list")),
#             ("Author detail", None),
#         ]
#         return breadcrumb_list


# class BookAuthorDeleteView(LoginRequiredMixin, DeleteView):
#     model = BookAuthor
#     template_name = "medialibrary/bookauthor_delete_confirm.html"
#     success_url = reverse_lazy("medialibrary:book-list")
#     context_object_name = "bookauthor"


# class BookListView(ListBreadcrumbMixin, LoginRequiredMixin, ListView):
#     model = Book
#     template_name = "medialibrary/book_list.html"
#     context_object_name = "books"
#
#     @cached_property
#     def crumbs(self):
#         breadcrumb_list = [
#             ("Dashboard", reverse_lazy("dashboard")),
#             ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
#             ("Books", reverse_lazy("medialibrary:book-list")),
#         ]
#         return breadcrumb_list


# class BookCreateView(CreateBreadcrumbMixin, LoginRequiredMixin, CreateView):
#     model = Book
#     template_name = "medialibrary/book_form.html"
#     form_class = BookForm
#     success_url = reverse_lazy("medialibrary:book-list")
#
#     @cached_property
#     def crumbs(self):
#         breadcrumb_list = [
#             ("Dashboard", reverse_lazy("dashboard")),
#             ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
#             ("Books", reverse_lazy("medialibrary:book-list")),
#             ("Create book", None),
#         ]
#         return breadcrumb_list


# class BookUpdateView(DetailBreadcrumbMixin, LoginRequiredMixin, UpdateView):
#     model = Book
#     template_name = "medialibrary/book_form.html"
#     form_class = BookForm
#     success_url = reverse_lazy("medialibrary:book-list")
#     context_object_name = "book"
#
#     @cached_property
#     def crumbs(self):
#         breadcrumb_list = [
#             ("Dashboard", reverse_lazy("dashboard")),
#             ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
#             ("Books", reverse_lazy("medialibrary:book-list")),
#             ("Update book", None),
#         ]
#         return breadcrumb_list


# class BookDetailView(DetailBreadcrumbMixin, LoginRequiredMixin, DetailView):
#     model = Book
#     template_name = "medialibrary/book_detail.html"
#     context_object_name = "book"
#
#     @cached_property
#     def crumbs(self):
#         breadcrumb_list = [
#             ("Dashboard", reverse_lazy("dashboard")),
#             ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
#             ("Books", reverse_lazy("medialibrary:book-list")),
#             ("Book detail", None),
#         ]
#         return breadcrumb_list


# class BookDeleteView(LoginRequiredMixin, DeleteView):
#     model = Book
#     template_name = "medialibrary/book_delete_confirm.html"
#     success_url = reverse_lazy("medialibrary:book-list")
#     context_object_name = "book"


# class MovieListView(ListBreadcrumbMixin, LoginRequiredMixin, ListView):
#     model = Movie
#     template_name = "medialibrary/movie_list.html"
#     context_object_name = "movies"
#
#     @cached_property
#     def crumbs(self):
#         breadcrumb_list = [
#             ("Dashboard", reverse_lazy("dashboard")),
#             ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
#             ("Movies", reverse_lazy("medialibrary:movie-list")),
#         ]
#         return breadcrumb_list


# class MovieCreateView(CreateBreadcrumbMixin, LoginRequiredMixin, CreateView):
#     model = Movie
#     template_name = "medialibrary/movie_form.html"
#     form_class = MovieForm
#     success_url = reverse_lazy("medialibrary:movie-list")
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     @cached_property
#     def crumbs(self):
#         breadcrumb_list = [
#             ("Dashboard", reverse_lazy("dashboard")),
#             ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
#             ("Movies", reverse_lazy("medialibrary:movie-list")),
#             ("Create movie", None),
#         ]
#         return breadcrumb_list


# class MovieUpdateView(DetailBreadcrumbMixin, LoginRequiredMixin, UpdateView):
#     model = Movie
#     template_name = "medialibrary/movie_form.html"
#     form_class = MovieForm
#     success_url = reverse_lazy("medialibrary:movie-list")
#     context_object_name = "movie"
#
#     @cached_property
#     def crumbs(self):
#         breadcrumb_list = [
#             ("Dashboard", reverse_lazy("dashboard")),
#             ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
#             ("Movies", reverse_lazy("medialibrary:movie-list")),
#             ("Update movie", None),
#         ]
#         return breadcrumb_list


# class MovieDetailView(DetailBreadcrumbMixin, LoginRequiredMixin, DetailView):
#     model = Movie
#     template_name = "medialibrary/movie_detail.html"
#     context_object_name = "movie"
#
#     @cached_property
#     def crumbs(self):
#         breadcrumb_list = [
#             ("Dashboard", reverse_lazy("dashboard")),
#             ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
#             ("Movies", reverse_lazy("medialibrary:movie-list")),
#             ("Movie detail", None),
#         ]
#         return breadcrumb_list


# class MovieDeleteView(LoginRequiredMixin, DeleteView):
#     model = Movie
#     template_name = "medialibrary/movie_delete_confirm.html"
#     success_url = reverse_lazy("medialibrary:movie-list")
#     context_object_name = "movie"
