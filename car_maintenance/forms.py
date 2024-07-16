from bootstrap_datepicker_plus.widgets import DatePickerInput, YearPickerInput
from django import forms

from .models import Car, CarMaintenanceHistory, FuelCosts


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "carmake",
            "carmodel",
            "year_of_production",
        ]
        widgets = {"year_of_production": YearPickerInput()}


class CarMaintenanceForm(forms.ModelForm):
    class Meta:
        model = CarMaintenanceHistory
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
            "fuelamount",
            "fuelcost",
            "odometer_reading",
        ]
        widgets = {"date": DatePickerInput()}
