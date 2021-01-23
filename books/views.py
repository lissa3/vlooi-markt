from django.shortcuts import render

from django.views.generic import TemplateView

class BookList(TemplateView):
    template_name = 'books/book_list.html'
