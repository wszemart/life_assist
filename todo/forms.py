from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(required=True)
    completed = forms.BooleanField(required=False)
    deadline = forms.DateField(widget=forms.DateInput(), required=False)

    class Meta:
        model = Task
        fields = [
            "title",
            "completed",
            "deadline",
        ]
