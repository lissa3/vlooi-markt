from django.test import TestCase
from django.db.models import When, Case, Count, Avg
from django.contrib.auth import get_user_model

from ..models import Category, Book
from .factories import (BookFactory, TagFactory, UserFactory,
                        UserWithBookFactory, AuthorFactory,
                        UserBookRelationFactory)

User = get_user_model()


class BookTest(TestCase):
    def test_book_creation(self):
        category = Category.objects.create(name="bar")
        user1 = UserFactory()
        user2 = UserFactory()
        book = BookFactory.create(
            category=category,
            authors=(AuthorFactory(), AuthorFactory()), tags=(TagFactory(), TagFactory()))
        user_book_rel1 = UserBookRelationFactory.create(book=book, user=user1)
        user_book_rel2 = UserBookRelationFactory.create(book=book, user=user2)
        self.assertEqual(2, book.clients.count())
        self.assertEqual(2, book.authors.count())
        self.assertEqual(2, book.tags.count())
