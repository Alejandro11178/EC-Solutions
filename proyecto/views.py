from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import usuario
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            user = authenticate(username=usuario.username, password=formulario.cleaned_data["password1"])
            if user is not None:
                login(request, user)  # Autenticar al usuario
                return redirect('home')
        else:
            data['form'] = formulario

    return render(request, 'registration/registro.html', data)





def user_login(request):
    return render(request, 'registration/login.html')

def registrar(request):
    registro = request.POST
    
    registro_nuevo = usuario.objects.create(
        nombre=registro['nombre'],
        apellido=registro['apellido'],
        correo=registro['correo'],
        contraseña=registro['contraseña'],
        es_profesor = registro['es_profesor'],
        materia = registro['materia'],
        nivel = registro['nivel'],
        horario = registro['horario'],
        precio=registro['registro']
    )
    return render(request, 'registration/registro.html')
    