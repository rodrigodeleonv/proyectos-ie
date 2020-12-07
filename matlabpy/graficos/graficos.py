"""Ejemplos con matplotlib"""

import matplotlib.pyplot as plt
import numpy as np

# # 1
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.legend()
# plt.show()
# # -------------------------------------------


# # 2
# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()
# # -------------------------------------------


# # 3
# def f(t):
#     """e^(-t) * Cos(2*Pi)"""
#     return np.exp(-t) * np.cos(2*np.pi*t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure()
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()
# # -------------------------------------------


# # 4
# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2*np.pi*t)
# line, = plt.plot(t, s, lw=2)
# plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#              arrowprops=dict(facecolor='black', shrink=0.05),
#              )

# plt.ylim(-2, 2)
# plt.show()
# # -------------------------------------------


# # 5
# # Seno
# x = np.arange(0, 4*np.pi, 0.1)  # start,stop,step
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()
# # -------------------------------------------


# # 6
# # Senos y cosenos misma grafica, titulos y leyendas
# x = np.arange(0, 4*np.pi, 0.1)  # start,stop,step
# y = np.sin(x)
# z = np.cos(x)
# plt.plot(x,y, x, z)
# plt.xlabel('x entre 0 - 4pi')
# plt.ylabel('sin(x) y cos(x)')
# plt.title('Gráfico de Seno y Coseno de 0 a 4pi')
# plt.legend(['sin(x)', 'cos(x)'])
# plt.grid(True,linewidth=0.5,color='#aaaaaa',linestyle='-')
# plt.show()
# # -------------------------------------------


# 7
x = np.linspace(-10, 10, 100)
y = x**2
plt.plot(x, y)
plt.xlabel('Parábola')
plt.ylabel('x^2')
plt.title('f(x) = x^2')
plt.grid(True,linewidth=0.5,color='#aaaaaa',linestyle='-')
plt.show()
# -------------------------------------------