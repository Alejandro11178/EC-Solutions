from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Room, Message

class RoomModelTest(TestCase):
    def test_room_creation(self):
        room = Room.objects.create(name='Sala de Pruebas', slug='sala-de-pruebas')
        self.assertEqual(room.name, 'Sala de Pruebas')
        self.assertEqual(room.slug, 'sala-de-pruebas')

    def test_room_str_method(self):
        room = Room.objects.create(name='Otra Sala', slug='otra-sala')
        self.assertEqual(str(room), 'Otra Sala')
class MessageModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            username='testuser',
            nombre='Test',
            apellidos='User',
            password='testpassword'
        )
        self.room = Room.objects.create(name='Sala de Pruebas', slug='sala-de-pruebas')
