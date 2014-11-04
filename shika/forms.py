from django.forms import ModelForm
from shika.models import Book

class BookEntryForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'is_lended']


