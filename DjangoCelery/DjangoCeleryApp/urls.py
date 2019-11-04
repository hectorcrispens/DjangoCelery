
from django.urls import path
from . import views

urlpatterns = [
    path('', views.prueba, name='nombre'),
    path('resp', views.resp, name='prueba')
]