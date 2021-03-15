from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=45, default="None")
    date_created = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(default=timezone.now)
    is_due = models.BooleanField(default=False)
    details = models.TextField(default="None")

class Subtasks(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    content = models.CharField(max_length=45, default="None")
