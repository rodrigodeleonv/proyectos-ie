from django.urls import path
from iot import views


app_name = 'iot'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.index, name='index'),
    path('json/random/', views.random_json, name='random_json'),
    path('files/imagen/', views.transferir_archivos, name='imagen1'),
    path('mostrar/sensores/', views.mostrar_sensores, name='sensores'),
    path('ajax/ejemplo/', views.ajax_ejemplo, name='ajax_ejemplo'),
    path('ajax/buttons/', views.ajax_buttons, name='ajax_buttons'),
    path('buttons/', views.web_botones),
]
