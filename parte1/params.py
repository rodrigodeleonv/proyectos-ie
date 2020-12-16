"""Uso de args y kwargs"""


def sumar1(valor1, valor2, valor3=0):
    print(f'Suma con parámetros posicionales: valor1={valor1} valor2={valor2}')
    return valor1 + valor2 + valor3


def sumar2(*args):
    print(f'Sumar con args: {args}. type(args)={type(args)}')
    s = 0
    for arg in args:
        s += arg
    # return s
    return sum(args)  # mas simple


def sumar3(**kwargs):
    print(f'Sumar con kwargs: {kwargs}. type(kwargs)={type(kwargs)}')
    suma = 0
    for key, value in kwargs.items():
        suma += value
    return suma


def sumar4(valor1, valor2, valor3=0, *args, **kwargs):
    print('Sumar valores posicionales, args y kwargs')
    print(f'Posicionales: valor1={valor1} valor2={valor2} valor3={valor3}')
    print(f'args={args}')
    print(f'kwargs={kwargs}')
    suma = valor1 + valor2 + valor3
    if args:
        suma = suma + sum(args)
    if kwargs:
        for key, value in kwargs.items():
            suma += value
    return suma


# print(f'sumar1: {sumar1(1, 2)}')
# print(f'sumar2: {sumar2(1, 2, 3, 4)}')
# print(f'sumar3: {sumar3(val1=1, val2=2, val3=3)}')
print(f'sumar4: {sumar4(1, 2, 3, 10, 20, kw1=100, kw2=200)}')
