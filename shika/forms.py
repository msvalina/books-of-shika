from django.forms import ModelForm
from shika.models import Book, LendingRequest

class BookEntryForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'is_lended']

class LendingRequestForm(ModelForm):

    class Meta:
        model = LendingRequest
        fields = ['book', 'book_owner', 'reader']

