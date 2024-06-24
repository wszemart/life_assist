from django.contrib import admin
from .models import Car, CarMaintenance, FuelCosts

admin.site.register(Car)
admin.site.register(CarMaintenance)
admin.site.register(FuelCosts)
