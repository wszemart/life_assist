from django.views.generic import UpdateView
from django.urls import reverse_lazy
from ...forms import CarForm
from ...models import Car


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_maintenance/car_form.html'
    form_class = CarForm
    success_url = reverse_lazy("car_maintenance:car-list")
    context_object_name = "car"
