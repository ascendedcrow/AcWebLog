
import django
from django.test import TestCase

from django.contrib.auth import get_user_model

class LoginTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(LoginTest, cls).setUpClass()
            django.setup()

    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_secure_page(self):
        return True
        User = get_user_model()
        self.client.login(username='temporary', password='temporary')
        self.assertEqual(self.client.request().is_authenticated(), False)
