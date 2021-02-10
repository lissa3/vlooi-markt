from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['authors', 'title', 'description', 'price', 'tags']

    def __init__(self, *args, **kwargs):
        # show categories choice in form (radio button)
        # treat input for one author (?checkboxes or dropdown?)
        # treat input for more than one author ( of just a string and to drop it to view for further validation
        # treat input for tags (as a list separated by ','
        # insert owner of the book == request user
        pass
