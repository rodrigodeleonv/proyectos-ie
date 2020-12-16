"""Ejecutar un sevidor web con Python"""

import os
from bottle import route, run


@route('/')  # colocar la ruta deseada del recurso
def root():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(BASE_DIR, 'index.html')
    with open(path, 'r') as file_page:
        content = file_page.read()
    print(content)
    return content


@route('/hello')
def hello():
    html = """
    <h1>Hola</h1>
    """
    return html


# Ejecutar el Servidor
# En el navegador: http://localhost:8080/ + Ruta
run(host='0.0.0.0', port=8000, debug=True)
