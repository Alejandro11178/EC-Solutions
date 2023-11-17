from django.test import TestCase, Client
from django.urls import reverse
from usuario.models import usuario
from room.models import Room, Message
from django.contrib.auth.models import User

class HomeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):

        self.user = usuario.objects.create(username='testuser', password='testpassword')
        self.client.force_login(self.user)

    def test_home_view_returns_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class RegistroViewTest(TestCase):
    def test_registro_view_returns_200(self):
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)

class ChatPaiViewTest(TestCase):
    def setUp(self):
        self.user = usuario.objects.create(username='testuser', password='testpassword')
        self.client.force_login(self.user)

    def test_chat_pai_view_returns_200(self):
        response = self.client.get(reverse('chat_pai'))
        self.assertEqual(response.status_code, 200)

