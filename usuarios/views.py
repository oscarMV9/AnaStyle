from .models import CustomUser
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect,render
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "este correo ya se encuentra registrado")
            return redirect('auth')
        
        if len(password) < 8:
            messages.error(request, "la contraseña es muy corta")
            return redirect('auth')
        
        if password != password_confirm:
            messages.error(request, "la contraseña no coincide intente de nuevo")
            return redirect('auth')
        
        CustomUser.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Usuario creado, por favor ingrese al sistema")
        return redirect('auth')
    return render(request, 'auth.html')

def ingreso(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            messages.success(request, f"Bienvenido {user.username}")
            return redirect('home')
        else:
            messages.error(request, "Ups, verifique sus credenciales")
            return redirect('ingreso')
    
    return render(request, 'ingreso.html')

def home(request):
    return render(request ,'home.html')