import requests

LETTER_NUMBER_MAP = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
    'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}


def letra_base(posicion, traslado=0):
    """
    BASE = 26
    Sea:
    c = 0       1       2
        A=1     A=27    A=53
        B=2     B=28    B=54
        C=3     C=29    C=55
        ...     ...     ...
        Z=26    Z=52    Z=78
    posicion = 26 * c + posicion_base + desplazamiento_lineal
    desplazamiento_lineal = 0
    c = ciclo
    c ~= int(posicion/26)
    """
    posicion_base = posicion - 26 * int(posicion/26)
    if posicion_base == 0:
        # se encuentra en c=1
        posicion_base = posicion
    print(posicion_base)
    return posicion_base


def retrasladar(translated, t=0):
    """
    Traslada las posiciones mayores a 27 a las posiciones base 1 a 26 del
    alfabeto
    """
    translated = translated.split(',')
    aux = list()
    for tran in translated:
        # print(f'tran: {tran}', type(tran))
        if tran.isdigit():
            tran_int = int(tran)
            c = int((tran_int - t) / 26)
            if c < 1:
                c = 1
            if tran_int > 26:
                position_base = tran_int - 26 * c - t
            else:
                position_base = tran_int - t
            # print(f'c={(tran_int-t) / 26}. c ~= {c}')
        else:
            position_base = tran
        if position_base == 0:
            position_base = 26
        aux.append(position_base)
    print(f'Posiciones base: {aux}')
    return aux


def text_converter(converted):
    mmap = dict((v, k) for k, v in LETTER_NUMBER_MAP.items())
    text = str()
    for conv in converted:
        try:
            text += mmap[conv]
        except KeyError:
            text += conv
    print(text)
    return text


def koorap_encrypt(word, initial, final):
    """
    Funcion que encripta mensaje:
    1. Texto en sentido inverso
    2. Reemplazar vocales por numeros
    3. Agregar caracteres al inicio y al final
    """
    replace_vowels = {
        'a': 0,
        'e': 1,
        'i': 2,
        'o': 3,
        'u': 4
    }
    keys = replace_vowels.keys()
    word_reversed = word[::-1]
    word_reversed = word_reversed.lower()
    encrypted = str()
    for repl in word_reversed:
        if repl in keys:
            encrypted += str(replace_vowels[repl])
        else:
            encrypted += repl
    encrypted = initial + encrypted + final
    # encrypted = encrypted.upper()
    print(f'encrypted: {encrypted}')
    return encrypted


def validate_with_server(encrypted, uuid, host):
    data = {
        'uuid': uuid,
        'encrypted': encrypted
    }
    response = requests.post(
        f'http://{host}/final/validate/',
        data=data
    )
    print(response.json())

#
# Ejecución del script
#


if __name__ == "__main__":
    # host = 'localhost:8000'
    host = 'rodrigodeleon.com:8610'
    carnet = ''

    for x in range(100):
        response = requests.get(
            f'http://{host}/final/mis_parametros/',
            params={'carnet': carnet}
        )
        mis_parametros = response.json()
        print(f'mis_parametros: {mis_parametros}')
        # traslado = int(mis_parametros['traslado'])  # traslado lineal
        traslado = 0  # ya no se usa, solo traslado ciclico
        inicial = mis_parametros['inicial']
        final = mis_parametros['final']

        url = f'http://{host}/final/'
        response = requests.get(url, params={'carnet': carnet})
        # if response.headers.get('content-type') != 'application/json':
        #     pass
        json_data = response.json()
        print(f'json_data: {json_data}')
        server_text = json_data['posicion_trasladada']
        uuid = json_data['uuid']
        retrasladado = retrasladar(server_text, traslado)
        texto = text_converter(retrasladado)
        encriptado = koorap_encrypt(texto, inicial, final)
        validate_with_server(encriptado, uuid, host)
