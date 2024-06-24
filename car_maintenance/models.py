from django.db import models
from datetime import datetime
from django.utils.timezone import now


class Car(models.Model):
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    year = models.DateField()

    def __str__(self) -> str:
        return f"{self.car_make} {self.car_model} {self.year}"


class CarMaintenance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    service = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.service} - ${self.cost}"


class FuelCosts(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField()
    fuel_amount = models.DecimalField(max_digits=5, decimal_places=2, help_text="in litres")
    fuel_cost = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField(help_text="in kilometers")

    def __str__(self):
        return f"{self.date} - {self.fuel_amount}L - ${self.cost} - {self.mileage}km"
