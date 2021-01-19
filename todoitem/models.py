from django.db import models
from todofolder.models import ToDoFolder


class ToDoItem(models.Model):
    description = models.CharField(max_length=255)
    checked = models.BooleanField(default=False)
    folder = models.ForeignKey(ToDoFolder, on_delete=models.CASCADE)
