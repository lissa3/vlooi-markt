# from django.shortcuts import redirect #render
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy

from .book_form import BookForm
from .models import Book

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from braces.views import SetHeadlineMixin #PrefetchRelatedMixin,


class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book


class BookCreate(SetHeadlineMixin,CreateView):
    form_class = BookForm
    headline = 'create'
    template_name = 'books/book_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Book created successfully!')
        response = super().form_valid(form)
        # if self.request.is_ajax():
        #     data = {"msg": "Submission successful"}
        #     print("success url", self.success_url)
        #     return JsonResponse({"redirect_to": self.success_url})
        # else:
        return response

    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong during book creation.')
        return super().form_valid(form)


class BookEdit(UpdateView):
    form_class = BookForm
    headline = 'edit'
    template_name = 'books/book_form.html'

    def get_queryset(self):
        # otherwise search for an object will be in whole qs
        # inclusive other users
        print("req user is",self.request.user)
        print("arr:",Book.objects.filter(owner=self.request.user))
        return Book.objects.filter(owner=self.request.user)


    def form_valid(self, form):
        # form.instance.owner = self.request.user
        messages.success(self.request, 'Book updated successfully!')
        response = super().form_valid(form)
        if self.request.is_ajax():
            msg = {"msg": "Edit successful"}
            print("success url", self.success_url)
            return JsonResponse({"redirect_to": self.success_url, "msg": msg})
        else:
            return response

    def form_invalid(self, form):
        """ If form is invalid return status 400 array of errors """
        messages.warning(self.request, 'Something went wrong during book editing.')
        response = super().form_valid(form)
        if self.request.is_ajax():
            msg = {"msg": "Something went wrong"}
            return JsonResponse({"msg": msg})
        else:
            return response
