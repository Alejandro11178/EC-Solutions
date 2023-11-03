from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import usuario

# Define un formulario personalizado para el registro de usuarios
class CustomUserCreationForm(UserCreationForm):
    # Agrega un campo de selección para el 'rol' del usuario
    rol = forms.ChoiceField(choices=[('alumno', 'Alumno'), ('profesor', 'Profesor')])
    materia = forms.CharField(max_length=255, required=False)
    horario = forms.CharField(max_length=255, required=False)
    nivel = forms.CharField(max_length=255, required=False)
    precio = forms.DecimalField(max_digits=6, decimal_places=0, required=False)
    telefono = forms.CharField(max_length=15, required=False)
    
    class Meta: 
        model = usuario  # Asocia el formulario con el modelo 'usuario'
        fields = ["rol", "nombre", "apellido", "correo", "telefono","password1", "password2", "materia", "horario", "nivel", "precio"]

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']

        # Verifica si el nombre de usuario ya existe en el modelo de usuario predeterminado
        if User.objects.filter(username=nombre).exists():
            raise forms.ValidationError('El nombre de usuario ya está en uso.')

        return nombre

