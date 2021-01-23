from django.urls import path
from .views import BookList

app_name = 'books'

urlpatterns = [
   path('books-list/',BookList.as_view(),name="book-list")
]