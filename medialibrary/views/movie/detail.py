from ...models import Movie
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from view_breadcrumbs import DetailBreadcrumbMixin


class MovieDetailView(DetailBreadcrumbMixin, LoginRequiredMixin, DetailView):
    model = Movie
    template_name = "medialibrary/movie_detail.html"
    context_object_name = "movie"

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
            ("Movies", reverse_lazy("medialibrary:movie-list")),
            ("Movie detail", None),
        ]
        return breadcrumb_list
