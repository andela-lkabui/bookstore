from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Category(models.Model):
    """Category ORM."""
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)


class Book(models.Model):
    """Book ORM."""
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)