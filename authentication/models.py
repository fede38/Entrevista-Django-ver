from django.db import models


class Usuario(models.Model):
    usuario = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
