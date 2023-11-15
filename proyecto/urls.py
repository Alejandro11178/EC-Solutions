from django.urls import path
from .views import Home, registro, Chat_pai, room

urlpatterns = [
    path('', Home.as_view(), name = 'index'),
    path('registro/', registro, name='registro'),
   
]
