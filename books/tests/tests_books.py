from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import Category,Author
from .factories import AuthorFactory,BookFactory

User = get_user_model()

class BookTest(TestCase):
    def test_book_creation(self):
        """warning: category based on mptt: had to do it manually"""
        category = Category.objects.create(name="bar")
        author=AuthorFactory()
        author_name = author.name
        book = BookFactory.create(category=category)
        book.authors.add(author)
        self.assertIn(author_name,str(book))


