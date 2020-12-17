from django.urls import path
from iot import views


app_name = 'iot'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
]
