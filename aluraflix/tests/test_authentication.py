from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthUserTest(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('João', password='123456')

    def test_user_auth(self):
        """Teste vireficação autenticação de um usuário correto"""
        user = authenticate(username='João', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_get_no_auth(self):
        """Teste para requisição GET não autenticada"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_user_name_incorrect(self):
        """Teste para nome incorreto"""
        user = authenticate(username='Joao', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_auth_user_pass_incorrect(self):
        """Teste para senha incorreta"""
        user = authenticate(username='João', password='123356')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_get_auth(self):
        """Teste para requisição GET autenticada"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)