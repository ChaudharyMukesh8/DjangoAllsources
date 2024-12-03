# emergency/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class EmergencyTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_report_emergency(self):
        response = self.client.post('/api/emergency/report/', {
            'latitude': 40.7128,
            'longitude': -74.0060
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Emergency reported successfully')

    def test_report_emergency_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/emergency/report/', {
            'latitude': 40.7128,
            'longitude': -74.0060
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
