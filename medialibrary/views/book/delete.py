from ...models import Book
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "medialibrary/book_delete_confirm.html"
    success_url = reverse_lazy("medialibrary:book-list")
    context_object_name = "book"
