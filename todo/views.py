from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from view_breadcrumbs import CreateBreadcrumbMixin, DetailBreadcrumbMixin, ListBreadcrumbMixin

from .forms import TaskCategoryForm, TaskForm
from .models import Task, TaskCategory


class TaskListView(ListBreadcrumbMixin, LoginRequiredMixin, ListView):
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


class TaskCreateView(CreateBreadcrumbMixin, LoginRequiredMixin, CreateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Tasks", reverse_lazy("todo:task-list")),
            ("Create task", None),
        ]
        return breadcrumb_list


class TaskUpdateView(DetailBreadcrumbMixin, LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Tasks", reverse_lazy("todo:task-list")),
            ("Update task", None),
        ]
        return breadcrumb_list


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TaskCategoryListView(ListBreadcrumbMixin, ListView):
    model = TaskCategory
    template_name = "todo/task_category_list.html"
    add_home = False

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Tasks", reverse_lazy("todo:task-list")),
            ("Tasks category list", reverse_lazy("todo:task-category-list")),
        ]
        return breadcrumb_list


class TaskCategoryCreateView(CreateBreadcrumbMixin, LoginRequiredMixin, CreateView):
    model = TaskCategory
    template_name = "todo/task_category_form.html"
    form_class = TaskCategoryForm
    success_url = reverse_lazy("todo:task-category-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.category_name = form.instance.category_name.upper()
        return super().form_valid(form)

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Tasks category list", reverse_lazy("todo:task-category-list")),
            ("Create new category", None),
        ]
        return breadcrumb_list


class TaskCategoryUpdateView(DetailBreadcrumbMixin, LoginRequiredMixin, UpdateView):
    model = TaskCategory
    template_name = "todo/task_category_form.html"
    form_class = TaskCategoryForm
    success_url = reverse_lazy("todo:task-category-list")

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Tasks category list", reverse_lazy("todo:task-category-list")),
            ("Update category", None),
        ]
        return breadcrumb_list


class TaskCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskCategory
    success_url = reverse_lazy("todo:task-category-list")
