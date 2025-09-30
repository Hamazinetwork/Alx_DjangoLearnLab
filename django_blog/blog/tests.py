from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AuthTests(TestCase):
    def test_register_login_logout(self):
# Register
        resp = self.client.post(reverse('register'), {
            'username': 'tester',
            'email': 'tester@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })
# After registration redirect to profile
        self.assertEqual(resp.status_code, 302)
# Login (client auto-logged in by view), check profile page
        resp = self.client.get(reverse('profile'))
        self.assertEqual(resp.status_code, 200)
# Logout
        resp = self.client.get(reverse('logout'))
# logout view often redirects
        self.assertIn(resp.status_code, (200, 302))


    def test_login_required_profile(self):
        resp = self.client.get(reverse('profile'))
# should redirect to login
        self.assertEqual(resp.status_code, 302)
        self.assertIn(reverse('login'), resp['Location'])
