""" Status models """
from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=30)
    slug_name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
