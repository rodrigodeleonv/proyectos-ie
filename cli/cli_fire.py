"""
CLI utilizando fire

python app.py sumar 1 2 3
"""

import fire
from numpy import prod


class Calculator:
    """Calculos elementales: sumar, restar, multiplicar, dividir
    """
    def sumar(self, *args):
        """Sumar cantidad arbitraria de numeros. Manejo de errores"""
        return sum(args)

    def restar(self, a, b):
        return a - b

    def multiplicar(self, *args):
        """Multiplica un conjunto de números dados"""
        return prod(args)


if __name__ == '__main__':
    fire.Fire(Calculator)
