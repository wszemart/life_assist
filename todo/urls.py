from django.urls import path

from .views import (
    TaskCategoryCreateView,
    TaskCategoryDeleteView,
    TaskCategoryListView,
    TaskCategoryUpdateView,
    TaskCreateView,
    TaskDeleteView,
    TaskListView,
    TaskUpdateView,
)

app_name = "todo"

urlpatterns = [
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="create-task"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task-category-list/", TaskCategoryListView.as_view(), name="task-category-list"),
    path("task-category/create/", TaskCategoryCreateView.as_view(), name="create-task-category"),
    path("task-category/<int:pk>/update/", TaskCategoryUpdateView.as_view(), name="task-category-update"),
    path("task-category/<int:pk>/delete/", TaskCategoryDeleteView.as_view(), name="task-category-delete"),
]
