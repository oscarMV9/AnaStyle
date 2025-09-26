from django.shortcuts import render


def indexPages(request):
    return render(request, 'inicio.html')

def productosPages(request):
    return render(request, 'productos.html')

def contactoPages(request):
    return render(request, 'contactenos.html')