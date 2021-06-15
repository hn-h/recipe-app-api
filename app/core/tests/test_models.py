from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test user created"""
        email = 'test@helloworld.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that email is normalized"""
        email = 'test@HELLOWORLD.COM'
        user = get_user_model().objects.create_user(email, 'Test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_no_email_raise_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test123')

    def test_create_superuser(self):
        email = 'test@helloworld.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_superuser(email, password)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
