from typing import Any

from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model."""

    class Meta:
        model = Task
        fields = ['id', 'title', 'is_completed']

    def validate_title(self, value: Any) -> str:
        """Ensure the title is not empty."""
        if not str(value).strip():
            raise serializers.ValidationError("Title cannot be empty")
        return str(value)
