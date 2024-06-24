from ...models import BookAuthor
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from view_breadcrumbs import DetailBreadcrumbMixin


class BookAuthorDetailView(DetailBreadcrumbMixin, LoginRequiredMixin, DetailView):
    model = BookAuthor
    template_name = "medialibrary/bookauthor_detail.html"
    context_object_name = "bookauthor"

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
            ("Books", reverse_lazy("medialibrary:book-list")),
            ("Author detail", None),
        ]
        return breadcrumb_list
