import os
from random import randint

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.conf import settings
from iot.models import Sensor, Measure


def home(request):
    """el parametro request, es obligatorio y django inserta
    el parametro como un objet HTTP Request
    """
    variable = 10
    response = f'Bienvenido {variable}, esta es la respuesta más simpole en la interfaz web'
    return HttpResponse(response)


class AboutView(View):
    def get(self, request):
        nombre = request.GET.get('name')
        carnet = request.GET.get('carnet', 201500123)
        response = 'Esta es una pagina donde se desarrollan e implementa '
        response += 'tecnologias IoT '
        response += f'Parametro nombre = {nombre}, carnet = {carnet}'
        return HttpResponse(response)


def index(request):
    context = {
        'variable1': 10,
        'variable2': 20,
        'lista': [1, 2, 3, 4, 5]
    }
    return render(request, 'iot/index.html', context)


def random_json(request):
    data = {
        'descripcion': 'Se genera un valor random',
        'response': 'Tipo Json',
        'comentario': 'Json es parecido a python dicts',
        'numero': randint(1, 1000),
    }
    return JsonResponse(data)


def transferir_archivos(request):
    path = os.path.join(settings.BASE_DIR, 'iot/static/iot/imagen.jpeg')
    f = open(path, 'rb')
    return FileResponse(f, as_attachment=True, filename='imagen.jpeg')


def mostrar_sensores(request):
    Sensor.objects.create(name=f'Presion{randint(10,1000)}',
                          tipo='Presion')
    # sensores = Sensor.objects.all()
    sensores = Sensor.objects.all().order_by('-id')[:10]  # Solo los 10 ultimos
    context = {
        'sensores': sensores,
    }
    return render(request, 'iot/mostrar_sensores.html', context)


def ajax_ejemplo(request):
    """Simple llamada por ajax desde Javascript hacia el servidor"""
    data = {
        'message': f'Mensaje del servidor. Código es: {randint(1000, 1000000)}'
    }
    return JsonResponse(data)


#
# Ejemplo de comunicación Javascript Ajax con Django Python de forma asincrona
#

def web_botones(request):
    """
    Envia una plantilla html con el codigo para que un navegador la muestre
    """
    context = {}
    return render(request, 'iot/web_botones.html', context)


@csrf_exempt  # para desactivar la seguridad que Django solicita por POST
def ajax_buttons(request):
    """
    A traves de Javascript, se enviara por AJAX un GET o POST con información
    de los botones presionados.

    Se generar una muestra de medición aleatoria para enviarse de vuelta a
    Javascript y que la muestra en la página en tiempo real.
    """
    boton_id = request.POST.get('boton_id', None)
    print(f'Boton id {boton_id}')

    if boton_id == 'boton1':
        # Acciones ....
        pass
    elif boton_id == 'boton2':
        # Acciones ....
        pass
    else:
        # Acciones ....
        pass

    # Guardar una muestra aleatoria. Debe existir al menos un sensor guardado
    # en la base de datos
    try:
        sensor = Sensor.objects.filter().last()
    except Sensor.DoesNotExist:
        sensor = None

    Measure.objects.create(
        sensor=sensor, value=randint(0, 100)
    )

    # Obtener las ultimas n muestras
    muestras = Measure.objects.order_by('-created')[:10]
    ultimas_mediciones = list()
    for muestra in muestras:
        ultimas_mediciones.append(muestra.value)
    # print(ultimas_mediciones)

    data = {
        'mediciones': ultimas_mediciones,
    }
    return JsonResponse(data)
