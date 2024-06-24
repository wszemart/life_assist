from ...models import Movie
from ...forms import MovieForm
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from view_breadcrumbs import DetailBreadcrumbMixin


class MovieUpdateView(DetailBreadcrumbMixin, LoginRequiredMixin, UpdateView):
    model = Movie
    template_name = "medialibrary/movie_form.html"
    form_class = MovieForm
    success_url = reverse_lazy("medialibrary:movie-list")
    context_object_name = "movie"

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Medialibrary", reverse_lazy("medialibrary:medialibrary")),
            ("Movies", reverse_lazy("medialibrary:movie-list")),
            ("Update movie", None),
        ]
        return breadcrumb_list
