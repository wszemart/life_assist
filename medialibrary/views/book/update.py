from ...models import Book
from ...forms import BookForm
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from view_breadcrumbs import DetailBreadcrumbMixin


class BookUpdateView(DetailBreadcrumbMixin, LoginRequiredMixin, UpdateView):
    model = Book
    template_name = "medialibrary/book_form.html"
    form_class = BookForm
    success_url = reverse_lazy("medialibrary:book-list")
    context_object_name = "book"

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
            ("Books", reverse_lazy("medialibrary:book-list")),
            ("Update book", None),
        ]
        return breadcrumb_list
