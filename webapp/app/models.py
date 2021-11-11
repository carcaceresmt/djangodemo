from django.db import models


# modelo de la app

class Calculadora(models.Model):
    n1 = models.FloatField()
    n2 = models.FloatField()

class rectangulo(models.Model):
    base = models.FloatField()
    altura = models.FloatField()


class Formula(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

