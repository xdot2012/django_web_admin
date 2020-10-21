from django.test import TestCase
from accounts.models import CustomUser

class CustomUserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(email="test_case_1@test.com", username="test_case_1", password="TEST123", is_superuser=True)
        CustomUser.objects.create(email="test_case_2@test.com", username="test_case_2", password="TEST123")

    def test_superusers(self):
        """Check for superusers"""
        user_1 = CustomUser.objects.get(username="test_case_1")
        user_2 = CustomUser.objects.get(username="test_case_2")
        self.assertEqual(user_1.is_superuser, True)
        self.assertEqual(user_2.is_superuser, False)
