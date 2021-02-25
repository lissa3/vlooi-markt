from books.models import Book
from rest_framework import serializers
from rest_framework import serializers as ser


class BookSerializer(ser.ModelSerializer):
    """catergory and owner: FK; authors: m2m """
    # owner = ser.URLField('get_absolute_url')
    class Meta:
        model = Book
        fields = ('category', 'title', 'description', 'authors', 'owner','price')
        depth = 1