from django import forms

from .models import Task, TaskCategory


class TaskForm(forms.ModelForm):
    category = forms.ModelChoiceField(required=True, queryset=TaskCategory.objects.all())
    title = forms.CharField(required=True)
    completed = forms.ChoiceField(required=True, choices=Task.COMPLETE_STATUS_CHOICES)
    deadline = forms.DateField(widget=forms.DateInput(), required=False)

    class Meta:
        model = Task
        fields = [
            "category",
            "title",
            "completed",
            "deadline",
        ]


class TaskCategoryForm(forms.ModelForm):
    category_name = forms.CharField(required=True)
    is_default = forms.BooleanField(required=True)

    class Meta:
        model = TaskCategory
        fields = [
            "category_name",
        ]
