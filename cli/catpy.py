"""
Emular el comando cat
leyendo archvio de texto e imprimiendolos en pantalla

Uso
python catpy.py leer </path/to/file>
"""

import fire


class LectorArchivos:
    """Emula el comportamiento de cat al leer archivos"""

    def leer(self, filename):
        """Lee el contenido de un archivo y retorna el contenido"""
        with open(filename, 'r') as file1:
            content = file1.read()
        return content


if __name__ == "__main__":
    fire.Fire(LectorArchivos)
