from django.urls import path
from .views import indexPages, productosPages, contactoPages

urlpatterns = [
    path('',indexPages, name='indexPage'),
    path('productos/', productosPages, name='productosPage'),
    path('contacto/', contactoPages, name='contactoPage'),
]