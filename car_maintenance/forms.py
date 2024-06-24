from bootstrap_datepicker_plus.widgets import DatePickerInput, YearPickerInput
from django import forms

from .models import Car, CarMaintenance, FuelCosts


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "car_make",
            "car_model",
            "year",
        ]
        widgets = {"year": YearPickerInput()}


class CarMaintenanceForm(forms.ModelForm):
    class Meta:
        model = CarMaintenance
        fields = [
            "car",
            "date",
            "service",
            "cost",
            "description",
        ]
        widgets = {"date": DatePickerInput()}


class FuelCostsForm(forms.ModelForm):
    class Meta:
        model = FuelCosts
        fields = [
            "car",
            "date",
            "fuel_amount",
            "fuel_cost",
            "mileage",
        ]
        widgets = {"date": DatePickerInput()}
