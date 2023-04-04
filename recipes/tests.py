from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

User = get_user_model()

class UserTestCase(TestCase):
    def SetUp(self):
        self.user_a = User.objects.create_user("codespaces", password='testme')