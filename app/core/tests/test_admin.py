from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from djang.test import Client

class AdminSideTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model.objects.create_superuser(
            email='admin@example.com', password='pass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model.objects.create_user(
        email='test@example.com', password='password123',
        name='Test user full name'
        )

    
