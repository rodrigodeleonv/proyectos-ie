"""
Laboratorio 2
Analisis de señales
Reconocimiento de Voz

Solución
"""

import requests
import speech_recognition as sr
import paho.mqtt.client as mqtt

URL = 'http://rodrigodeleon.com:8610/users/topic'


def on_connect(client, userdata, flags, rc):
    """Callback."""
    if rc == 0:
        print("connected OK Returned code=", rc)
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, rc):
    print(f'Ha ocurrido una desconexión! rc={rc}')


def on_publish(client, userdata, result):
    print('Publicado!')


def on_message(client, userdata, message):
    """Callback. Cada nuevo mensaje recibido se ejecuta la función"""
    print(f'Mensaje recibido {str(message.payload.decode("utf-8"))}')
    print(
        f'Topic {message.topic}',
        f'QoS {message.qos}', f'retain={message.retain}'
    )
    print('\n')


r = sr.Recognizer()
mic = sr.Microphone()
# sr.Microphone.list_microphone_names()
with mic as source:
    print('Ajustando ruido ambiental')
    r.adjust_for_ambient_noise(source)
    print('Grabando audio...')
    audio = r.listen(source)
    print('Audio grabado')
data = r.recognize_google(audio, language='es-GT')

params = {
    'username': '',
    'password': ''
}
response = requests.get(URL, params=params)
json_data = response.json()
topic = json_data['topic']

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_message = on_message
client.connect(host='rodrigodeleon.com', port=8601, keepalive=5)
client.loop_start()
client.publish(topic, data)
client.loop_stop()
client.disconnect()
