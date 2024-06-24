from ...models import Book
from ...forms import BookForm
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from view_breadcrumbs import CreateBreadcrumbMixin


class BookCreateView(CreateBreadcrumbMixin, LoginRequiredMixin, CreateView):
    model = Book
    template_name = "medialibrary/book_form.html"
    form_class = BookForm
    success_url = reverse_lazy("medialibrary:book-list")

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
            ("Books", reverse_lazy("medialibrary:book-list")),
            ("Create book", None),
        ]
        return breadcrumb_list
