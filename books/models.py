from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=250)


class Tag(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)

    def __str__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=250)


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='cat_books')
    authors = models.ManyToManyField('Author',related_name="authour_books")
    unid = models.CharField(max_length=8, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    title = models.CharField(max_length=250)
    in_stock = models.BooleanField(default=True)
    description = models.CharField(blank=True, max_length=1024, default="")
    tags = models.ManyToManyField(Tag, blank=True, related_name='tag_books')

    def __str__(self):
        return f"{self.title} written by {self.author}. Price {self.price}"

    def get_absolute_url(self, *args, **kwargs):
        return reverse('books:book_detail', kwargs={'unid': self.unid})
