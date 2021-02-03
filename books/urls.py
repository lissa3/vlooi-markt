from django.urls import path
from .views import BookList,BookDetail

app_name = 'books'

urlpatterns = [
   path('books-list/',BookList.as_view(),name="book-list"),
   path('books-detail/<slug:slug>',BookDetail.as_view(),name="book-detail")
]