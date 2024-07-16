from django.contrib import admin
from .models import Car, CarMaintenanceHistory, FuelCosts

admin.site.register(Car)
admin.site.register(CarMaintenanceHistory)
admin.site.register(FuelCosts)
