# from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


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