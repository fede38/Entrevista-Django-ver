from django.db import models


class ToDoFolder(models.Model):
    description = models.CharField(max_length=255)
