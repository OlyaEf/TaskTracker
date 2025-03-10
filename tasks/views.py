from rest_framework import generics

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskListCreateAPIView(generics.ListCreateAPIView):
    """API view for listing and creating tasks."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
