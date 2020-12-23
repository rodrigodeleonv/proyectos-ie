"""
Laboratorio 2
Subscriber

"""
import os
import requests
import paho.mqtt.client as mqtt

BASE_DIR = os.path.dirname(__file__)

BROKER_ADDRESS = 'rodrigodeleon.com'
PORT = 8601

# URL = 'http://localhost:8000/users/ingreso_nota'
URL = F'http://{BROKER_ADDRESS}:8610/users/ingreso_nota'

# Sucribiendo a todos los topics
TOPIC = 'Proyectos-ie/Labs/2/#'


def ingresar_nota(carnet, value, frase='Vacio'):
    data = {
        'value': value,
        'score_type': 'L2',
        'carnet': carnet,
        'comment': frase
    }
    response = requests.post(
        URL,
        data=data
    )
    print(response.json())


# Callbacks

def on_connect(client, userdata, flags, rc):
    """Callback. Cada vez que se conecte/reconecte ejecuta la funcion"""
    print(f"Re/Suscribing to TOPIC: {TOPIC}")
    client.subscribe(TOPIC)
    if rc == 0:
        print(f'Connected OK Returned code={rc}')
    else:
        print('Bad connection Returned code={rc}')


def on_disconnect(client, userdata, rc):
    """Callback. Si ocurre una desconexión se ejecuta la función"""
    print(f'Ha ocurrido una desconexión! rc={rc}')


def on_message(client, userdata, message):
    """Callback. Cada nuevo mensaje recibido se ejecuta la función"""
    carnet = message.topic.split('/')[3]
    payload = str(message.payload.decode("utf-8"))
    ingresar_nota(carnet, value=100, frase=payload)
    print(f'Topic {message.topic}')
    print(f'Mensaje recibido: {payload}')
    print('\n')
    filepath = os.path.join(BASE_DIR, 'logs', f'{carnet}.txt')
    with open(filepath, 'a+') as log:
        log.write(f'{payload}\n')


# Script

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect(host=BROKER_ADDRESS, port=PORT, keepalive=10)
client.subscribe(TOPIC)

try:
    client.loop_forever()  # Blocking
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
