from django.views.generic import TemplateView


# from books.mixins import DisplayCategoryMixin


class HomePage(TemplateView):
    template_name = 'home.html'


class Banned(TemplateView):
    template_name = 'forbidden403.html'
