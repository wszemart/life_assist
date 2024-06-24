from ...models import BookAuthor
from ...forms import BookAuthorForm
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from view_breadcrumbs import CreateBreadcrumbMixin


class BookAuthorCreateView(CreateBreadcrumbMixin, LoginRequiredMixin, CreateView):
    model = BookAuthor
    template_name = "medialibrary/bookauthor_form.html"
    form_class = BookAuthorForm
    success_url = reverse_lazy("medialibrary:book-list")

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
            ("Books", reverse_lazy("medialibrary:book-list")),
            ("Create author", None),
        ]
        return breadcrumb_list
