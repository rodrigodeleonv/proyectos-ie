"""
Docstring del módulo.

Módulo de Sensores
"""

import random


def sumar(param1, param2):
    return param1 + param2


class Sensor:
    """Clase que representa un sensor generico"""

    nombre = None
    modelo = None

    def __init__(self, nombre, modelo=None):
        self.nombre = nombre
        self.modelo = modelo

    def mostrar_nombre(self):
        return self.nombre

    def __str__(self):
        return f'Sensor, {self.nombre} modelo={self.modelo} '


class SensorTemperatura(Sensor):
    def medir(self):
        return random.randint(-20, 100)


if __name__ == "__main__":
    sensor1 = Sensor(nombre='Sensor1')
    print(sensor1)

    temperatura = SensorTemperatura('Temperatura1', modelo='TR1')

    medir = temperatura.medir()
    print(f'Temperatura actual es: {medir}')



