from django.shortcuts import redirect  # render
from django.contrib import messages
from django.http import JsonResponse
# from django.urls import reverse_lazy

from .book_form import BookForm
from .models import Book, Category

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from braces.views import SetHeadlineMixin  # PrefetchRelatedMixin,


# from users.mixins import UserPassesBannedView


class BookCategory(ListView):
    """List of products based on category (slug)"""
    template_name = "books/book_list.html"
    paginate_by = 5

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        node = Category.objects.get(slug=slug)
        if Book.objects.filter(category__slug=slug).exists():
            print("block if calling")
            book_list = Book.objects.filter(category__slug=slug)
        else:
            print("block else calling")
            # no clear why I need this filter
            book_list = Book.objects.filter(category__slug__in=[x.slug for x in node.get_family()])
        return book_list


class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book


# Note thx dj-braces use the same template for rendering form create + update
# class BookCreate(LoginRequiredMixin, UserPassesTestMixin, SetHeadlineMixin, CreateView):
#  At this point no message about banned status (neither with custom mixin, nor native UserPTM)
class BookCreate(LoginRequiredMixin, SetHeadlineMixin, CreateView):
    form_class = BookForm
    headline = 'create'
    template_name = 'books/book_form.html'

    # def test_func(self):
    #     return not self.request.user.banned

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


class BookEdit(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
# class BookEdit(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    form_class = BookForm
    headline = 'edit'
    template_name = 'books/book_form.html'

    def test_func(self):
        obj = self.get_object()
        var1 = obj.owner == self.request.user
        var2 = not self.request.user.banned
        if var1 and var2:
            return True
        else:
            messages.error( self.request, 'You do not have permission to view the previous page.')
        # return var1 and var2

    def get_queryset(self):
        # otherwise search for an object will be in whole qs
        # inclusive other users
        print("req user is", self.request.user)
        print("is this user banned?", self.request.user.banned)
        # print("arr:", Book.objects.filter(owner=self.request.user))
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
