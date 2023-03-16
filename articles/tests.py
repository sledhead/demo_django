from django.test import TestCase

# Create your tests here.

from .models import Article

class ArticleTestCase(TestCase):

    def setUp(self):
        self.number_of_articles = 5
        for i in range(0,self.number_of_articles):
            Article.objects.create(title='Test Title', content='simple message for testing things')

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual( qs.count(), self.number_of_articles )