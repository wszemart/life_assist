from django.urls import path
from .views import task_list, TaskCreateView

urlpatterns = [
    path('tasks/', task_list, name='task-list'),
    path('create_task/', TaskCreateView.as_view(), name='create-task'),
]
