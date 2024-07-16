from django.views.generic import DeleteView
from django.urls import reverse_lazy
from ...models import Car


class CarDeleteView(DeleteView):
    model = Car
    template_name = "car_maintenance/car_delete_confirm.html"
    success_url = reverse_lazy("car_maintenance:car-list")
    context_object_name = "car"
