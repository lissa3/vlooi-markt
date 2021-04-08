import factory
import faker
from django.contrib.auth import get_user_model

from factory.django import DjangoModelFactory

from books.models import Author, Book, UserBookRelation, Category,Tag

User = get_user_model()

fake = faker.Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'username_{}'.format(n))
    email = factory.LazyAttribute(lambda o: '%s@example.com' % o.username)

class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag
    name = factory.Faker('word')

class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker('name')


class BookFactory(DjangoModelFactory):
    """dif ways to fill title/description/text"""
    class Meta:
        model = Book

    title = factory.lazy_attribute(lambda n: ' '.join(fake.words(nb=3)))
    description = factory.Faker('sentence', nb_words=3, variable_nb_words=True)
    price = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    in_stock = factory.Faker('pybool')
    on_sale = factory.Faker('pybool')
    owner = factory.SubFactory(UserFactory)
    # no success with decorator ...hm ...
    # @factory.post_generation
    # def authors(self, create, extracted, **kwargs):
    #     print("inside decorator")
    #     if not create:
    #         return
    #     if extracted:
    #         for _ in range(2):  # <- if you want more than one
    #             self.authors.add(AuthorFactory())
    #             self.refresh_from_db()





class UserBookRelationFactory(DjangoModelFactory):
    class Meta:
        model = UserBookRelation

    user = factory.SubFactory(UserFactory)
    book = factory.SubFactory(BookFactory)
    rating = 5
    likes = True

# class UserWithGroupFactory(UserFactory):
#     membership = factory.RelatedFactory(GroupLevelFactory, 'user')
#
# class UserWith2GroupsFactory(UserFactory):
#     membership1 = factory.RelatedFactory(GroupLevelFactory, 'user', group__name='Group1')
#     membership2 = factory.RelatedFactory(GroupLevelFactory, 'user', group__name='Group2')
