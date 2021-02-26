from books.models import Book
from rest_framework import serializers
from rest_framework import serializers as ser


class BookSerializer(ser.ModelSerializer):
    """catergory and owner: FK; authors: m2m """
    # category = ser.URLField('get_absolute_url')
    # url = ser.CharField(source='get_absolute_url', read_only=True)
    # "url": "/books/books-detail/best-choice-of-room-plants"
    class Meta:
        model = Book
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        fields = ('category', 'title', 'slug','description', 'authors', 'owner','price','url')
        # depth = 1
"""
{
    "category": 8,
    "title": "Best choice of room plants",
    "slug": "best-choice-of-room-plants",
    "description": ...",
    "authors": [3],
    "owner": 3,
    "price": "...",
    "url": "http://127.0.0.1:8000/api/v1/books/best-choice-of-room-plants/"
}
"""