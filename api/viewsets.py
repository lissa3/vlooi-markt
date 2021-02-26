from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializer import BookSerializer
from books.models import Book, Category, Author
from django.contrib.auth import get_user_model

User = get_user_model()


class BookViewset(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated] # checks auth; if OK|=> perform_create starts
    serializer_class = BookSerializer
    lookup_field = 'slug'
    queryset = Book.objects.all()

   # def create /perform_create: extra layer of validation ( excl duble; type or like that

    def create(self, request):
        """ create (basic req.data ) vs perform_create (no req.data;suitable for custom-n)
         and has serialiser"""
        data = request.data
        category_id = data.get('category_id')
        category = get_object_or_404(Category, id=category_id)
        owner_id = data.get('owner_id')
        owner = get_object_or_404(User, id=owner_id)
        price = data.get('price')
        title = data.get('title')
        desc = data.get('description')
        authors = data.get('authors') # list [{'name': 'Mulya'}]
        new_book = Book.objects.create(
            owner=owner, category=category, title=title, description=desc, price=price
        )
        list_authors = []
        for person in authors:
            for n,name_val in person.items():
                if Author.objects.filter(name=name_val).exists():
                    found_author = get_object_or_404(Author,name=name_val)
                    new_book.authors.add(found_author)
                else:
                    new_author = Author.objects.create(name=name_val)
                    new_book.add(new_author)
        new_book.save()
        serializer = BookSerializer(new_book)
        return Response(serializer.data)

    # def perform_create(self, serializer):
    #     """ create (basic req.data ) vs perform_create (no req.data;suitable for custom-n)
    #      and has serialiser"""
    #     req_data = self.request.data
    #     #serializer.validated_data: title,descr-n,price; no trace of FK or m2m
    #     data = serializer.validated_data
    #     category_id = req_data.get('category_id')
    #     # category_id = data.get('category_id') # here None
    #     category = get_object_or_404(Category, id=category_id)
    #     print("found cat", category)
    #     owner_id = req_data.get('owner_id')
    #     owner = get_object_or_404(User, id=owner_id)
    #     print("found owner", owner)
    #     author_id = req_data.get('author_id')
    #     author = get_object_or_404(Author,id=author_id)
    #     # serializer.save(owner=owner, category=category)
    #     print("It's done ....")



