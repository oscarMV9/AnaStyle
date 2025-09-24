from django.urls import path
from .views import indexPages, productosPages

urlpatterns = [
    path('',indexPages, name='indexPage'),
    path('/productos', productosPages, name='productosPage'),
]