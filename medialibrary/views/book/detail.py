from ...models import Book
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from view_breadcrumbs import DetailBreadcrumbMixin


class BookDetailView(DetailBreadcrumbMixin, LoginRequiredMixin, DetailView):
    model = Book
    template_name = "medialibrary/book_detail.html"
    context_object_name = "book"

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
            ("Books", reverse_lazy("medialibrary:book-list")),
            ("Book detail", None),
        ]
        return breadcrumb_list
