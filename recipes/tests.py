from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import RecipeIngredient, Recipe

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
        self.recipe_a = Recipe.objects.create(name='Pulled beef', user=self.user_a)

    def test_user_count(self):
        
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_recipe_reserve_count(self):
        user = self.user_a
        qs = user.recipe_set.all()
        print(qs)
        self.assertEqual(qs.count(), 1)

    
    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        print(qs)
        self.assertEqual(qs.count(), 1)

