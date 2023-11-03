from django.db import models

# Define el modelo 'usuario' que hereda de 'models.Model'
class usuario(models.Model):
    # Define las opciones para el campo 'rol'
    ROL_CHOICES = [
        ('alumno', 'Alumno'),
        ('profesor', 'Profesor'),
    ]
    
    # Define los campos del modelo 'usuario'
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    contraseña = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='alumno')
    materia = models.CharField(max_length=255)
    nivel = models.CharField(max_length=255)
    horario = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=6, decimal_places=0)
    
    # Especifica el campo 'nombre' como el campo de usuario personalizado
    USERNAME_FIELD = 'nombre'

    def __str__(self):
        return self.nombre
