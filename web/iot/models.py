from django.db import models


class Sensor(models.Model):
    """
    La clase sensor de Python represtan una tabla de la base de datos
    Atributos de la clase representan los campos de la tabla
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)  # Humedad, presion, ultrasonico

    def __str__(self):
        return f'Sensor: {self.name} tipo={self.tipo}'


class Measure(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    value = models.FloatField(default=0)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return f'Medición: {self.value} | sensor={self.sensor.name}'


class MqttLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.message}'
