from ...models import Book
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from view_breadcrumbs import ListBreadcrumbMixin


class BookListView(ListBreadcrumbMixin, LoginRequiredMixin, ListView):
    model = Book
    template_name = "medialibrary/book_list.html"
    context_object_name = "books"

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
            ("Books", reverse_lazy("medialibrary:book-list")),
        ]
        return breadcrumb_list
