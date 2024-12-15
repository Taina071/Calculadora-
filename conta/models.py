from django.db import models

class Calculo(models.Model):
    resultado = models.FloatField()

    def __str__(self):
        return f"Resultado: {self.resultado}"