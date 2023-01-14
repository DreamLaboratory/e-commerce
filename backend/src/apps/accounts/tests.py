from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            phone_number="997707375", username="admin", first_name="admin", last_name="admin", password="foo"
        )
        self.assertEqual(user.phone_number, "997707375")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            phone_number="997707375", username="admin", first_name="admin", last_name="admin", password="foo"
        )
        self.assertEqual(admin_user.phone_number, "997707375")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
