from django.db import models


class Task(models.Model):
    """Task model."""
    title: str = models.CharField(max_length=100)
    is_completed: bool = models.BooleanField(default=False)

    def __str__(self):
        return self.title
