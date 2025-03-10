from django.urls import path

from tasks.views import TaskListCreateAPIView

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
]
