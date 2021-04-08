from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import Category,Author
from .factories import AuthorFactory,BookFactory,TagFactory

User = get_user_model()

class BookTest(TestCase):
    def test_book_creation(self):
        """warning: category based on mptt: had to do it manually"""
        category = Category.objects.create(name="bar")
        author=AuthorFactory()
        tag = TagFactory()
        author_name = author.name
        book = BookFactory.create(category=category)
        book.authors.add(author)
        book.tags.add(tag)
        self.assertIn(author_name,str(book))
        self.assertEqual(tag,book.tags.get(name=tag))


