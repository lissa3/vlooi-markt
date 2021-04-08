from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import Category
from .factories import BookFactory,UserFactory,UserWithBookFactory,AuthorFactory

User = get_user_model()

class BookTest(TestCase):
    def test_book_creation(self):
        """warning: category based on mptt: had to do it manually"""
        category = Category.objects.create(name="bar")
        author1 = AuthorFactory()
        author2 = AuthorFactory()
        book = BookFactory.create(category=category,authors=(author1,author2))
        print(book.authors.all())
        self.assertEqual(2,book.authors.count())
        # self.assertEqual(2,book.tags.count())


        # obj = UserWithBookFactory()
        # print(vars(obj))



