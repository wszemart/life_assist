from django.urls import path

from .views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView

app_name = "car_maintenance"

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car-list'),
    path('cars/new/', CarCreateView.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
]
