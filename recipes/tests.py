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
        self.recipe_b = Recipe.objects.create(name='Pulled beef sandwich', user=self.user_a)
        self.recipe_c = Recipe.objects.create(name='steamed carrots', user=self.user_a)

        self.recipe_ingredient_a = RecipeIngredient.objects.create(recipe=self.recipe_a, name='Beef', quantity='1/4', unit='pound')

    def test_user_count(self):
        
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_recipe_reserve_count(self):
        user = self.user_a
        qs = user.recipe_set.all()
        print(qs)
        self.assertEqual(qs.count(), 3)

    
    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        print(qs)
        self.assertEqual(qs.count(), 3)

    
    def test_recipe_ingredient_reserve_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingredient_set.all()
        print(qs)
        self.assertEqual(qs.count(), 1)

    def test_recipe_ingredient_count(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe=recipe)
        print(qs)
        self.assertEqual(qs.count(), 1)

    def test_user_two_level_relation(self):
        user = self.user_a
        qs = RecipeIngredient.objects.filter(recipe__user=user)
        self.assertEqual(qs.count(), 1)

    def test_user_two_level_relation_reserve(self):
        user = self.user_a
        recipe_ingredient_ids = user.recipe_set.all().values_list('adklsd', flat=True)
        print(recipe_ingredient_ids)
        #qs = RecipeIngredient.objects.filter(recipe__user=user)
        self.assertEqual(recipe_ingredient_ids.count(), 1)


