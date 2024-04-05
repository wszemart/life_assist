from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import TaskCategoryForm, TaskForm
from .models import Task, TaskCategory


class TaskListView(ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "object_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        for task in queryset:
            task.color = Task.STATUS_COLORS.get(task.completed, "")
        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskCategoryListView(ListView):
    model = TaskCategory
    template_name = "todo/task_category_list.html"


class TaskCategoryCreateView(LoginRequiredMixin, CreateView):
    model = TaskCategory
    template_name = "todo/task_category_form.html"
    form_class = TaskCategoryForm
    success_url = reverse_lazy("task-category-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
