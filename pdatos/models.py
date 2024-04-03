from django.db import models

# Create your models here.

class bdatos(models.Model):
    tamanio = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    estacionamiento = models.IntegerField()
    piscina = models.IntegerField()
    distrito = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)


class Sdatos(models.Model):
    tamanio = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    estacionamiento = models.IntegerField()
    piscina = models.IntegerField()
    distrito = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)