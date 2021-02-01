from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
# from utils.common import TimeStamp



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

#
# class Book(TimeStamp):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_books')
#     authors = models.ManyToManyField('Author',related_name="authour_books")
#     unid = models.CharField(max_length=8, blank=True)
#     slug = AutoSlugField(populate_from='title', unique=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner_books')
#     title = models.CharField(max_length=250)
#     description = models.TextField(blank=True, default="")
#     in_stock = models.BooleanField(default=True)
#     on_sale = models.BooleanField(default=False)
#     tags = models.ManyToManyField(Tag, blank=True, related_name='tag_books')
#
#     def __str__(self):
#         return f"{self.title} written by {self.author}. Price {self.price}"
#
#     def get_absolute_url(self, *args, **kwargs):
#         return reverse('books:book_detail', kwargs={'unid': self.unid})
