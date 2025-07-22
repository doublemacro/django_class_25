from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from books.models import Book
from books.serializers import BookSerializer
from rest_framework import viewsets

# Create your views here.

fruits = ['Apple', 'Pineapple', 'Durian', 'Passion fruit', 'Banana', 'Pear']

def hello(request):
    return HttpResponse("Hello from our Books app!")

def home(request):
    # Django -> Jinja(Template Engine)

    context = {
        'username': 'Alice',
        'logged_in': True,
        'current_time': datetime.now(),
        'fruits': fruits
    }

    return render(request, 'home.html', context)

def create_book(request):
    book1 = Book()
    book1.title = "Hello"
    book1.author = "Jack"
    book1.page_count = 30
    book1.save()
    return HttpResponse("DONE")

def about(request):
    return render(request, 'about.html')


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


