from django.urls import path
from .views import registro, ingreso, home

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('ingreso/', ingreso, name='ingreso'),
    path('home/',home, name='home'),
]