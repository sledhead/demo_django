import os
from django.conf import settings
from django.test import TestCase

class TryDjangoConfigTest( TestCase ):

    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get('SECRET_KEY')
        self.assertNotEqual(SECRET_KEY,'abc1223')