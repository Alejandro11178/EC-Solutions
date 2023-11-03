from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import usuario

# Define las vistas para la aplicación

# Vista de inicio de la página
def home(request):
    """
    Renderiza la página de inicio de la aplicación.
    """
    return render(request, 'core/home.html')

# Vista de registro de usuarios
def registro(request):
    """
    Maneja el proceso de registro de usuarios.
    Crea un nuevo usuario utilizando el modelo de usuario predeterminado y luego crea un usuario personalizado
    asignando los campos restantes. Después, autentica al usuario y lo redirige a la página de inicio.
    """
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            # Crea un nuevo usuario utilizando el modelo de usuario predeterminado
            user = User(username=formulario.cleaned_data['nombre'])
            user.set_password(formulario.cleaned_data["password1"])
            user.save()

            # Crea un usuario personalizado y asigna los otros campos
            custom_user = usuario(
                nombre=formulario.cleaned_data['nombre'],
                apellido=formulario.cleaned_data['apellido'],
                correo=formulario.cleaned_data['correo'],
                telefono=formulario.cleaned_data['telefono'],
                rol=formulario.cleaned_data['rol'],
                materia=formulario.cleaned_data['materia'],
                nivel=formulario.cleaned_data['nivel'],
                horario=formulario.cleaned_data['horario'],
                precio=formulario.cleaned_data['precio']
            )
            custom_user.save()

            # Autentica al usuario recién creado y redirige a la página de inicio
            user = authenticate(username=custom_user.nombre, password=formulario.cleaned_data["password1"])
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            data['form'] = formulario

    return render(request, 'registration/registro.html', data)

# Vista de inicio de sesión de usuarios
def user_login(request):
    """
    Renderiza la página de inicio de sesión de usuarios.
    """
    return render(request, 'registration/login.html')
