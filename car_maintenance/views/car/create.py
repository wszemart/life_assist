from django.views.generic import CreateView
from django.urls import reverse_lazy
from ...forms import CarForm
from ...models import Car


class CarCreateView(CreateView):
    model = Car
    template_name = 'car_maintenance/car_form.html'
    form_class = CarForm
    success_url = reverse_lazy("car_maintenance:car-list")