from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import usuario
from room.models import Room
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.views.generic import CreateView, ListView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import FormLogin, ProfesorForm, AlumnoForm
from django.contrib import messages


class loginUsuario(FormView):
    template_name = 'usuario/login.html'
    form_class = FormLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(loginUsuario, self).dispatch(request,*args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(loginUsuario,self).form_valid(form)
    
def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')




class RegistrarProfesor(CreateView):
    model = usuario
    form_class = ProfesorForm
    template_name = 'usuario/registroProf.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Crear una sala asociada al profesor recién creado
        nueva_sala = Room.objects.create(name=f"Sala de {self.object.username}", slug=f"sala-{self.object.username}")

        # Asociar la sala con el profesor
        self.object.room = nueva_sala
        self.object.save()

        messages.success(self.request, '¡Registro exitoso! Ahora eres un profesor y tienes una sala asociada.')

        return response

    

class RegistrarAlumno(CreateView):
    model = usuario
    form_class = AlumnoForm
    template_name = 'usuario/registroAlum.html'
    success_url = reverse_lazy('login')

    

