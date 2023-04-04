from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user("snowman", password='goatman')

    def test_user_pw(self):
        checked = self.user_a.check_password('goatman')
        self.assertTrue(checked)

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user("snowman", password='25snow99')

    def test_user_count(self):
        
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

