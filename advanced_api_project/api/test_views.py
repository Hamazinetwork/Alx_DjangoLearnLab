from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book


class BookAPITests(APITestCase):

    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username="testuser", password="pass123")
        self.admin = User.objects.create_superuser(username="admin", password="admin123")

        # Create an author
        self.author = Author.objects.create(name="George Orwell")

        # Create some books
        self.book1 = Book.objects.create(title="1984", publication_year=1949, author=self.author)
        self.book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author)

        # Endpoints
        self.list_url = reverse("book-list")
        self.create_url = reverse("book-create")
        self.detail_url = reverse("book-detail", args=[self.book1.id])
        self.update_url = reverse("book-update", args=[self.book1.id])
        self.delete_url = reverse("book-delete", args=[self.book1.id])

    # ---------- CRUD TESTS ----------

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_create_book_requires_authentication(self):
        data = {"title": "New Book", "publication_year": 2020, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="pass123")
        data = {"title": "New Book", "publication_year": 2020, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="pass123")
        data = {"title": "Updated 1984", "publication_year": 1949, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated 1984")

    def test_delete_book_requires_authentication(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="pass123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------- FILTERING / SEARCH / ORDERING ----------

    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.list_url, {"publication_year": 1949})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {"search": "Animal"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Animal Farm")

    def test_order_books_by_title(self):
        response = self.client.get(self.list_url, {"ordering": "title"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, ["1984", "Animal Farm"])  # alphabetically ordered
