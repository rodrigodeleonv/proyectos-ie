"""Programa que mide la conexión de internet"""

import speedtest

speed = speedtest.Speedtest()

option = int(input('''¿Qué te guspeedaría medir?:
1) Download Speed
2) Upload Speed
3) Ping
Elige: '''))

print('Iniciando medición. Espere....')
if option == 1:
    down = speed.download() / 1024 / 1024
    print(f'{down} Mbps')
elif option == 2:
    up = speed.upload() / 1024 / 1024
    print(f'{up} Mbps')
elif option == 3:
    servernames = []
    speed.get_servers(servernames)
    print(speed.results.ping)
else:
    print("Elige una opción correcta!")
