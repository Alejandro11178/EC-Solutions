"""
URL configuration for ProfeDelivery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuario.views import loginUsuario, logoutUsuario
from proyecto.views import room
from django.contrib.auth.decorators import login_required
from proyecto import views
from proyecto.views import Chat_pai

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include(('usuario.urls','usuario'))),
    path('proyecto/',include(('proyecto.urls','proyecto'))),
    path('',views.Home.as_view(), name = 'index'),
    path('accounts/login/',loginUsuario.as_view(),name='login'),
    path('logout/',login_required(logoutUsuario), name='logout'),
    path('mensajeria/<slug:slug>', room , name='room' ),
    path('mensajeria/chat/', Chat_pai , name='chat'),
    path('chat_pai/', views.Chat_pai, name='chat_pai'),
    path('home/', views.Home.as_view(), name='home'),
    path('registro/', views.registro, name='registro'),

]
