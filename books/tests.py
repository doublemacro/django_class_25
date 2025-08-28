import pytest
from books.models import Book
from django.contrib.auth import get_user_model

@pytest.fixture
def user(db):
    # get_user_model() -> User
    return get_user_model().objects.create_user(username="adrian", password="tomato12345")

@pytest.fixture
def logged_in_client(client, user):
    client.login(username="adrian", password="tomato12345")
    return client

def test_book_creation(db, user):
    saved_book = Book.objects.create(title="Book hello", author="Test", page_count=300, created_by=user)

    db_book = Book.objects.first()
    assert saved_book.title == db_book.title

# fixture
@pytest.fixture
def book_obj(user):
    book1 = Book(title="Book 1", author="Jamal", page_count=300, created_by=user)
    book1.save()
    return book1

def test_check_thing1(book_obj):
    assert book_obj.title == "Book 1"
    assert True

def test_check_book(book_obj):
    assert book_obj.author == "Jamal"

@pytest.mark.django_db
def test_delete_book_confirm_page(logged_in_client, book_obj):
    url = "/books/{}/delete/".format(book_obj.pk)
    response = logged_in_client.get(url)
    assert response.status_code == 200
    assert "Are you sure you want to delete this book?" in response.text


@pytest.mark.django_db
def test_delete_book(logged_in_client, book_obj):
    url = "/books/{}/delete/".format(book_obj.pk)
    # Check if book actually exists in db
    assert Book.objects.filter(pk=book_obj.pk).exists() == True
    # make POST request to server to delete the book
    response = logged_in_client.post(url)
    assert response.status_code == 302
    # check if book has been deleted from DB
    assert Book.objects.filter(pk=book_obj.pk).exists() == False

@pytest.mark.django_db
def test_update_book(logged_in_client, book_obj):
    url = "/books/{}/edit/".format(book_obj.pk)

    response = logged_in_client.post(url, {
        "title": "Updated Title",
        "author": "Updated Author",
        "page_count": 321
    })

    assert response.status_code == 302

    book_obj.refresh_from_db()
    assert book_obj.title == "Updated Title"
    assert book_obj.author == "Updated Author"
    assert book_obj.page_count == 321
