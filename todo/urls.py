from django.urls import path
from .views import TaskCreateView, TaskListView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('create-task/', TaskCreateView.as_view(), name='create-task'),
]
