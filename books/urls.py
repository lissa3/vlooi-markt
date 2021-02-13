from django.urls import path
from .views_with_mixin_cats import BookList,BookDetail,BookCreate,BookEdit,BookCategory

app_name = 'books'

urlpatterns = [
   path('books-list/',BookList.as_view(),name="book-list"),
   path('create-book/',BookCreate.as_view(),name="book-create"),
   path('books-detail/<slug:slug>',BookDetail.as_view(),name="book-detail"),
   path('books-edit/<slug:slug>',BookEdit.as_view(),name="book-edit"),
   path('category-books/<slug:slug>',BookCategory.as_view(),name="cats-list")
]