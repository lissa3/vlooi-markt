from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from myutils.models import TimeStamp
from django.urls import reverse

User = get_user_model()


# from django.shortcuts import reverse

class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=60, db_index=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self,*kwargs):
    #     return reverse('')


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Book(TimeStamp):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_books')
    authors = models.ManyToManyField('Author', related_name="authour_books")
    unid = models.CharField(max_length=8, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_books')
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, default="")
    in_stock = models.BooleanField(default=True)
    on_sale = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tag_books')
    clients = models.ManyToManyField(User, through='UserBookRelation')

    def __str__(self):
        first_author = self.authors.first().name
        if self.authors.count() == 1:
            str_authors = f"{first_author}"
        else:
            str_authors = f"{first_author} and others"
        #TODO: methods to list all authors
        #for obj in self.authors.all():
        #         names.append(obj.name)
        #names = " ".join(names)

        return f"'{self.title}' written by {str_authors}."

    def get_absolute_url(self, *args, **kwargs):
        return reverse('books:book-detail', kwargs={'slug': self.slug})


class UserBookRelation(models.Model):
    RATING = (
        (1, 'Low'),
        (2, 'OK'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Excellent')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    likes = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(choices=RATING, null=True)

    def __str__(self):
        return f'User: {self.user.username} gives rating: {self.rating} for this product.'
