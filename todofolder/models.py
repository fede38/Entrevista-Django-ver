from django.db import models
from authentication.models import Usuario


class ToDoFolder(models.Model):
    description = models.CharField(max_length=255)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
