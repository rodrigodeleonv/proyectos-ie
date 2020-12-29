from django.db import models


class EjemploMedicion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    valor = models.FloatField(default=0)

    def __str__(self):
        return f'EjemploMedicion: {self.valor}'
