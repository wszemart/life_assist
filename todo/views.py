from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, DeleteView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task-list")

    def form_valid(self, form: TaskForm):
        form.instance.author = self.request.user
        return super().form_valid(form)

