"""
MQTT Ejemplo
Publisher
Require: Servidor Broker MQTT
Instalación paquete: pip install paho-mqtt

rc = return code
0: Connection successful
1: Connection refused – incorrect protocol version
2: Connection refused – invalid client identifier
3: Connection refused – server unavailable
4: Connection refused – bad username or password
5: Connection refused – not authorised
6-255: Currently unused.

MQTT puerto por defecto: 1883
"""

from time import sleep
import paho.mqtt.client as mqtt

# Brokers MQTT public for tests. No hay garantia
# BROKER_ADDRESS = "iot.eclipse.org"
# BROKER_ADDRESS = 'broker.emqx.io'
# PORT = 1883

# Broker personal
# BROKER_ADDRESS = '3.17.240.64'
BROKER_ADDRESS = 'rodrigodeleon.com'
PORT = 8601

TOPIC = 'proyectos-ie/clase/mqtt-ejemplo'


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
    print(f'Topic {message.topic}',
          f'QoS {message.qos}', f'retain={message.retain}')
    print('\n')


print('Creando nueva instancia')
# client = mqtt.Client("PyMQTTProjectosIE-123")  # debe ser único!
client = mqtt.Client()  # Genera id único automáticamente

# Binding to Callbacks
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_message = on_message

print('Conectando al Broker')
client.connect(host=BROKER_ADDRESS, port=PORT, keepalive=10)

# Asincrono, non-blocking
# Se reconecta automaticamente si se pierde la conexión
client.loop_start()

print(f'Publicando mensaje en Topic {TOPIC}')
counter = 0
while True:
    counter += 1
    try:
        print(f'COMANDO{counter}\n')
        client.publish(TOPIC, f'COMANDO{counter}')
        sleep(1)  # publicar cada x segundos
    except KeyboardInterrupt:
        break

client.loop_stop()
client.disconnect()
print('Conexión finalizada')
