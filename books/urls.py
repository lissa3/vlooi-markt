from django.urls import path
from .views import BookList,BookDetail,BookCreate

app_name = 'books'

urlpatterns = [
   path('books-list/',BookList.as_view(),name="book-list"),
   path('create-book/',BookCreate.as_view(),name="book-create"),
   path('books-detail/<slug:slug>',BookDetail.as_view(),name="book-detail")
]