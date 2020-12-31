"""
Decodificador Morse:

1. Solicita codigos al servidor
2. Decodifica y suma los valores
3. Devuelve al servidor el resultado
"""

import requests
from time import sleep

# mappers es un archivo hecho a mano para relacioanar morse
# y valores numericos asigados a cada letra del alfabeto
from mappers import MORSE_CODE_MAP, LETTER_NUMBER_MAP


CARNET = ''

URL_get = 'http://rodrigodeleon.com:8610/users/morse/'
URL_post = 'http://rodrigodeleon.com:8610/users/morse/verify/'


def get_morse(carnet=CARNET, url=URL_get):
    """
    Solicita al servidor los códigos morse, a traves de una http request.
    El servidor devuelve un JSON de los cuales los valores:
        code, uuid
    son relevantes.
    """
    data = {
        'carnet': carnet
    }
    response = requests.get(url, params=data)
    json_data = response.json()
    code = json_data['code']
    uuid = json_data['uuid']
    # print(code)
    return uuid, code


def registrar_resultado(uuid, result, url=URL_post):
    """
    Envia al servidor la suma de los código morse, para que los registre
    """
    data = {
        'uuid': uuid,
        'result': result
    }
    response = requests.post(url, data=data)
    json_data = response.json()
    print(json_data)
    return json_data


def morse_decoder(code):
    """
    Decodificador de codigo morse, utiliza mapeo de diccionarios para
    relacionar CODIGO_MORSE --> LETRA.
    Luego utiliza la funciona navita sum(...) para sumar la lista de LETRAS
    almacenadas en la lista numbers.
    """
    code_list = code.split()
    letters = str()
    numbers = list()
    for morse_code in code_list:
        letters += MORSE_CODE_MAP[morse_code]
        numbers.append(LETTER_NUMBER_MAP[MORSE_CODE_MAP[morse_code]])
    return letters, numbers, sum(numbers)


if __name__ == "__main__":
    cnt_valid = 0
    cnt_no_valid = 0
    for i in range(100):
        uuid, code = get_morse()
        _, _, result = morse_decoder(code)
        json_response = registrar_resultado(uuid, result)
        if json_response['valid'] is False:
            print(f'No valido: {result} {uuid}')
            cnt_no_valid += 1
        else:
            cnt_valid += 1
        sleep(0.5)
    print(f'Validos {cnt_valid}. No validos {cnt_no_valid}')
