from ...models import BookAuthor
from ...forms import BookAuthorForm
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from view_breadcrumbs import DetailBreadcrumbMixin


class BookAuthorUpdateView(DetailBreadcrumbMixin, LoginRequiredMixin, UpdateView):
    model = BookAuthor
    template_name = "medialibrary/bookauthor_form.html"
    form_class = BookAuthorForm
    success_url = reverse_lazy("medialibrary:book-list")
    context_object_name = "bookauthor"

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
            ("Books", reverse_lazy("medialibrary:book-list")),
            ("Update author", None),
        ]
        return breadcrumb_list
