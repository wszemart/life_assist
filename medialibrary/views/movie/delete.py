from ...models import Movie
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = "medialibrary/movie_delete_confirm.html"
    success_url = reverse_lazy("medialibrary:movie-list")
    context_object_name = "movie"
