from django.db import models
from datetime import datetime
from django.utils.timezone import now


class Car(models.Model):
    carmake = models.CharField(max_length=100)
    carmodel = models.CharField(max_length=100)
    year_of_production = models.DateField()
    #owner=user

    def __str__(self) -> str:
        return f"{self.carmake} {self.carmodel} {self.year_of_production}"


class CarMaintenanceHistory(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='maintenancehistory')
    date = models.DateField(default=now)
    service = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.service} - ${self.cost}"


class FuelCosts(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField()
    fuelamount = models.DecimalField(max_digits=5, decimal_places=2, help_text="in litres")
    fuelcost = models.DecimalField(max_digits=10, decimal_places=2)
    odometer_reading = models.IntegerField(help_text="total mileage in kilometers", null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.fuelamount}L - ${self.fuelcost}"
