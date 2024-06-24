from ...models import BookAuthor
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView


class BookAuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = BookAuthor
    template_name = "medialibrary/bookauthor_delete_confirm.html"
    success_url = reverse_lazy("medialibrary:book-list")
    context_object_name = "bookauthor"
