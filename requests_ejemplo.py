"""
Cliente http
"""

import requests

URL = 'http://127.0.0.1:8000/ejemplo/responder_json/'


data = {
    'carnet': '201563258',
    'nombre': 'Juan Perez',
    'edad': 20
}

response = requests.post(URL, data=data)

json_data = response.json()
print(json_data)
print(f'El tipo de datos de respuesta es {type(json_data)}')
print(
    json_data['code'], json_data['parametro2'], json_data['parametro3'])