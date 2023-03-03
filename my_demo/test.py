import os
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.test import TestCase

class TryDjangoConfigTest( TestCase ):

    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get('SECRET_KEY')
        #self.assertNotEqual(SECRET_KEY,'abc122')

        try:
            is_strong = validate_password(SECRET_KEY)

        except Exception as e:
            msg = f'Bad Secret Key {e.messages}'
            self.fail(msg)