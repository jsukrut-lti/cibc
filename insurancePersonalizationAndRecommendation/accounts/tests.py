from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
                username='will',
                email='will@skp.com',
                password='testpass123'
        )
        self.assertEqual(user.username,'will')
        self.assertEqual(user.email,'will@skp.com')
        self.assertEqual(user.password,'testpass123')

        admin_user = User.objects.create_user(
                username='superAdmin',
                email='sa@skp.com',
                password='testpass123'
        )
        self.assertTrue(admin_user.is_superuser)