from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    description = forms.CharField(
        help_text='give a short description for your product'
    )
    price = forms.DecimalField(
        help_text='Price will be displayed in US dollars'
    )
    class Meta:
        model = Book
        fields = ['category','authors', 'title', 'description', 'price'] #, 'tags']

    # def __init__(self, *args, **kwargs):
    #     # show category choice in form (radio button) Now = default = dropdown
    #     # treat input for one author (?checkboxes or dropdown?)
    #     # treat input for more than one author ( of just a string and to drop it to view for further validation
    #     # treat input for tags (as a list separated by ','
    #     # insert owner of the book == request user
    #     pass
    # tags = MyFormField(
    #     max_length=200,
    #     required=False,
    #     help_text='Please, enter tag(s), separated by comma ","',
    # )
