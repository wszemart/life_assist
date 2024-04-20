from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from view_breadcrumbs import BaseBreadcrumbMixin

from .forms import TaskCategoryForm, TaskForm
from .models import Task, TaskCategory


class TaskListView(BaseBreadcrumbMixin, LoginRequiredMixin, ListView):
    model = Task
    template_name = "todo/task_list.html"
    add_home = False

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Tasks", reverse_lazy("todo:task-list")),
        ]
        return breadcrumb_list


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task-list")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")


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
        form.instance.category_name = form.instance.category_name.upper()
        return super().form_valid(form)


class TaskCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskCategory
    template_name = "todo/task_category_form.html"
    form_class = TaskCategoryForm
    success_url = reverse_lazy("task-category-list")


class TaskCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskCategory
    success_url = reverse_lazy("task-category-list")
