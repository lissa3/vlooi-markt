from django.views.generic import TemplateView
from books.mixins import DisplayCategoryMixin


class HomePage(DisplayCategoryMixin, TemplateView):
    template_name = 'home.html'
