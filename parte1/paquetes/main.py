"""Modulo principal para ejecutar la aplicacion"""

from constantes.matematicas import PI
from sensores.externos import SensorTemperatura

temperatura = SensorTemperatura('T1', 'TR1')

if __name__ == "__main__":
    print(f'La temperatura actual es: {temperatura.medir()}')


vscode
python3.8 (para el sistema operativo que utilicen, Linux (WSL2) VM) <<---PIP
Crear una cuenta en Github si no la tienen
Git