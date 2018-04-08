from django.forms import ModelForm
from crm.models import Book


class Bookform(ModelForm):
    """書籍のForm"""
    class Meta:
        model = Book
        field = ('name', 'publisher', 'page', )
