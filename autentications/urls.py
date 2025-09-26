from django.urls import path
from .views import registro, ingreso,home,logout_view

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('ingreso/', ingreso, name='ingreso'),
    path('logout/', logout_view, name='logout'),
    path('home/', home, name='home'),
]