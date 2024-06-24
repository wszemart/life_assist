from ...models import Movie
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from view_breadcrumbs import ListBreadcrumbMixin


class MovieListView(ListBreadcrumbMixin, LoginRequiredMixin, ListView):
    model = Movie
    template_name = "medialibrary/movie_list.html"
    context_object_name = "movies"

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
            ("Movies", reverse_lazy("medialibrary:movie-list")),
        ]
        return breadcrumb_list
