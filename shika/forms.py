from django.forms import ModelForm
from shika.models import Book, LendingRequest

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'is_lended']

class LendingRequestForm(ModelForm):
    class Meta:
        model = LendingRequest
        fields = ['book', 'reader']
