from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CarForm, CarMaintenanceForm, FuelCostsForm
from .models import Car, CarMaintenance, FuelCosts

#
class CarListView(ListView):
    model = Car
    template_name = 'car_maintenance/car_list.html'
    context_object_name = 'cars'


class CarCreateView(CreateView):
    model = Car
    template_name = 'car_maintenance/car_form.html'
    form_class = CarForm
    success_url = reverse_lazy("car_maintenance:car-list")


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_maintenance/car_form.html'
    form_class = CarForm
    success_url = reverse_lazy("car_maintenance:car-list")
    context_object_name = "car"


class CarDeleteView(DeleteView):
    model = Car
    template_name = "car_maintenance/car_delete_confirm.html"
    success_url = reverse_lazy("car_maintenance:car-list")
    context_object_name = "car"


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_maintenance/car_detail.html'
    context_object_name = 'car'
