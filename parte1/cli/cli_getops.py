"""
CLI usando getops
"""

import sys
import getopt


class Calc:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        return a / b


# Definimos los parámetros de cli que deseamos

# cuando hay ":" significa que la opción requiere un argumento
shortopts = 'a:b:'
# empiezan con --, ejemplo: --help
# cuando hay "=" significa que la opción requiere un argumento
longopts = ['help', 'sumar=', 'restar=', 'multiplicar=', 'dividir=',]

argv = sys.argv[1:]  # Descartando el primero
opts, args = getopt.getopt(argv, shortopts=shortopts, longopts=longopts)

print('Opciones y parametros recibidos')
print('-------------------------------')
print(f'opts: {opts}')
print(f'args: {args}')
print('-------------------------------\n')

calc = Calc()

for opt, arg in opts:
    if opt in ['-h', '--help']:
        print('Help')
    elif opt in ['-s', '--sumar']:
        resultado = calc.sumar(args[0], args[1])
        print(f'Resultado {resultado}')
    # elif opt in