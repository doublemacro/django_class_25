from django import forms
from books.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['thumbnail_image', 'title', 'author', 'page_count']

