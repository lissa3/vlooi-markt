# from django.shortcuts import render
from .book_form import BookForm
from .models import Book

from django.views.generic import ListView, DetailView, CreateView


class BookList(ListView):
    model = Book
    # context_object_name = 'book_list'
    # template_name = 'books/book_list.html'


class BookDetail(DetailView):
    model = Book
    # context_object_name = 'book'
    # template_name = 'books/book_detail.html'


class BookCreate(CreateView):
    form_class = BookForm
    template_name = 'books/book_form.html'
    
    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


