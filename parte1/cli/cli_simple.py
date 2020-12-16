"""
Argumentos de linea de comandos

Modulo recibe argumentos de linea de comandos

Módulo sys proporciona funciones y variables que se usan
para manipular diferntes partes de Runtime de python y
acceso a ciertas partes del interprete.
"""

import sys


class Calc:
    """Provee metodos para operaciones basicas"""

    def sumar(self, a, b):
        return int(a) + int(b)

    def restar(self, a, b):
        return int(a) - int(b)

    def multiplicar(self, a, b):
        return int(a) * int(b)

    def dividir(self, a, b):
        return int(a) / int(b)


print('Parametros recibidos -------------------------')
# sys.argv[0] siempre devuelve el nombre del script
print(f'nombre de este modulo sys.argv[0] = {sys.argv[0]}')
print('Todos los argumentos recibidos:', sys.argv[1:])


calculadora = Calc()
argumentos = sys.argv[1:]


if sys.argv[1] == 'sumar':
    resultado = calculadora.sumar(sys.argv[2], sys.argv[3])
    print(resultado)
elif sys.argv[1] == 'restar':
    resultado = calculadora.restar(sys.argv[2], sys.argv[3])
    print(resultado)
elif sys.argv[1] == 'multiplicar':
    resultado = calculadora.multiplicar(sys.argv[2], sys.argv[3])
    print(resultado)
elif sys.argv[1] == 'dividir':
    resultado = calculadora.dividir(sys.argv[2], sys.argv[3])
    print(resultado)
elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("""
Programa de línea de comandos. Operaciones basicas.
Parámetros
#####################
sumar:          a + b
restar:         a - b
multiplicar:    a * b
dividir:        a / b
#####################
          """)