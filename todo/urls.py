from django.urls import path

from .views import TaskCategoryCreateView, TaskCategoryListView, TaskCreateView, TaskListView

urlpatterns = [
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("create-task/", TaskCreateView.as_view(), name="create-task"),
    path("task-category-list/", TaskCategoryListView.as_view(), name="task-category-list"),
    path("create-task-category/", TaskCategoryCreateView.as_view(), name="create-task-category"),
]
