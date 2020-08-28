import json

#   django import
from django.contrib.auth.models import User
from django.test import TestCase

#   restframework case tests
from rest_framework.test import RequestsClient
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.


class UserSetUp:

    @staticmethod
    def start_user():
        u = User.objects.create(username="django", email="django@django.com")
        u.set_password('django')
        u.save()


class APISetUp:

    @staticmethod
    def get_auth_client():
        client = APIClient()

        response = client.post(
            '/api/v1/login/', {'username': 'django', "password": "django"}, format='json')

        token_access = response.data['access']

        client.credentials(
            HTTP_AUTHORIZATION=f'Bearer ' + token_access)

        return client

    @staticmethod
    def create_fake_sender():

        client = APISetUp.get_auth_client()

        payload = {
            "recipient": "16997376614",
            "kind_message": "SMS",
            "msg": "Olá Por favor envie algo"
        }

        response = client.post(
            '/api/v1/sendrequest/', payload, format='json')


class AuthenticationTestCase(TestCase):

    def setUp(self):
        """
        Description
        -----------
        """

        UserSetUp.start_user()

        self.client = APIClient()

    def test_token_obtain(self):

        response = self.client.post(
            '/api/v1/login/', {'username': 'django', "password": "django"}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refreash_token(self):
        pass
        # self.client.credentials(HTTP_AUTHORIZATION=f'Bearer ' + self.token_access)

        # response = self.client.post('/api/v1/login/refresh/')

        # self.assertEqual(response.status_code, status.HTTP_200_OK)


class SendRequestEndpoint(TestCase):

    def setUp(self):
        UserSetUp.start_user()

        self.client = APISetUp.get_auth_client()

    def test_list_rigth(self):

        response = self.client.get(
            '/api/v1/sendrequest/', data={'format': 'json'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_rigth(self):

        payload = {
            "recipient": "16997376614",
            "kind_message": "SMS",
            "msg": "Olá Por favor envie algo"
        }

        response = self.client.post(
            '/api/v1/sendrequest/', payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrive_rigth(self):
        APISetUp.create_fake_sender()

        response = self.client.get(
            '/api/v1/sendrequest/2/', data={'format': 'json'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    