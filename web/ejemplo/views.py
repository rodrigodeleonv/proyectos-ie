from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ejemplo.models import EjemploMedicion
import random


def index(request):
    return JsonResponse({})


def vista1(request):
    context = {}
    return render(request, 'ejemplo/e1.html', context)


@csrf_exempt
def json_ejemplo(request):
    boton_id = request.POST.get('boton_id', None)
    print(f'boton_id: {boton_id}')
    # carnet = request.POST.get('carnet', None)
    # nombre = request.POST.get('nombre', None)
    # edad = request.POST.get('edad', None)
    # print(carnet, nombre, edad)
    # data = {
    #     'parametro1': 'Valor1',
    #     'parametro2': 10,
    #     'parametro3': None,
    # }

    valor_aleatorio = random.randint(10, 50)  # 10, 11, ... 50
    EjemploMedicion.objects.create(valor=valor_aleatorio)

    mediciones = EjemploMedicion.objects.order_by('-created')[:5]
    temporal = list()
    for medicion in mediciones:
        temporal.append(medicion.valor)
    data = {
        'mediciones': temporal
    }
    # print(temporal)
    return JsonResponse(data)
