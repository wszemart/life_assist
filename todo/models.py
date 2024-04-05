from django.contrib.auth.models import User
from django.db import models


class TaskCategory(models.Model):
    category_name = models.CharField(max_length=100, help_text="Name of the task category", unique=True)
    is_default = models.BooleanField(default=False, help_text="Is this a default category?")

    def save(self, *args, **kwargs):
        self.category_name = self.category_name.upper()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Task(models.Model):
    COMPLETE_STATUS_CHOICES = [
        ("TO_DO", "To Do"),
        ("IN_PROGRESS", "In Progress"),
        ("DONE", "Done"),
        ("BLOCKED", "Blocked"),
    ]

    STATUS_COLORS = {
        "TO_DO": "lightgoldenrodyellow",
        "IN_PROGRESS": "lightblue",
        "DONE": "lightgreen",
        "BLOCKED": "lightcoral",
    }

    title = models.CharField(max_length=200, help_text="Title of the task")
    completed = models.CharField(max_length=100, choices=COMPLETE_STATUS_CHOICES, help_text="Task status")
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE, help_text="Task category")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date of task create")
    deadline = models.DateTimeField(blank=True, null=True, help_text="Deadline of the task")
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Author of the task")

    def __str__(self):
        return self.title
