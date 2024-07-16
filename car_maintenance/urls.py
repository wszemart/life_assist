from django.urls import path

from car_maintenance.views.car.create import CarCreateView
from car_maintenance.views.car.delete import CarDeleteView
from car_maintenance.views.car.detail import CarDetailView
from car_maintenance.views.car.list import CarListView
from car_maintenance.views.car.update import CarUpdateView
from .dash import app

app_name = "car_maintenance"

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car-list'),
    path('cars/new/', CarCreateView.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
]
