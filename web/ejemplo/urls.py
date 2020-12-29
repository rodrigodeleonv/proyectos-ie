from django.urls import path
from ejemplo import views


app_name = 'ejemplo'

urlpatterns = [
    path('', views.index),
    path('responder_json/', views.json_ejemplo, name='json_ejemplo'),
    path('e1/', views.vista1, name='e1'),
]
