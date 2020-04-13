from django.db import models

# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    pokemon_type = models.CharField(max_length=100)
    weakness = models.CharField(max_length=50)
    lvl = models.IntegerField()
    description = models.TextField(max_length=250)
