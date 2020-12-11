"""
CLI:

Grafica la función f(x) = (x - a) * (x - b)
que insertecta en y=0, los puntos a y b

Uso:
python script.py parabola -2 3
"""

import matplotlib.pyplot as plt
import numpy as np
from fire import Fire


class Graph:
    def parabola(self, a, b):
        """Plotea"""
        a = int(a)
        b = int(b)
        print(f'Argumentos: {a} {b}')
        x = np.linspace(a - 1, b + 1, 100)
        y = (x - a) * (x - b)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Parábola que corta a y=0 en {a} y {b}')
        plt.grid(True, linewidth=0.5, color='#aaaaaa', linestyle='-')
        plt.show()
        return 'f(x) graficado'

if __name__ == "__main__":
    Fire(Graph)
