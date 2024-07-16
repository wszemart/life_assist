from django.views.generic import DetailView
from ...models import Car


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_maintenance/car_detail.html'
    # context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = Car.objects.all()  # Dodanie listy wszystkich samochodów do kontekstu
        return context
