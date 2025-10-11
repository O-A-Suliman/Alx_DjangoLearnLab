from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    """✅ Unit Tests for Book API endpoints (CRUD + Filters + Search + Ordering)"""

    def setUp(self):
        """Set up test data before each test runs"""
        self.user = User.objects.create_user(username="tester", password="12345")

        self.author = Author.objects.create(name="J.K. Rowling")

        self.book1 = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author,
        )
        self.book2 = Book.objects.create(
            title="Harry Potter and the Chamber of Secrets",
            publication_year=1998,
            author=self.author,
        )

        # URLs for endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book1.id])

    # ------------------- CRUD TESTS -------------------

    def test_list_books(self):
        """✅ Test GET all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_book(self):
        """✅ Test GET single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book_authenticated(self):
        """✅ Test POST (create) requires authentication"""
        self.client.login(username="tester", password="12345")
        data = {
            "title": "Harry Potter and the Prisoner of Azkaban",
            "publication_year": 1999,
            "author": self.author.id,
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        """✅ Test PUT (update)"""
        self.client.login(username="tester", password="12345")
        data = {
            "title": "Harry Potter Updated",
            "publication_year": 1997,
            "author": self.author.id,
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Harry Potter Updated")

    def test_delete_book_authenticated(self):
        """✅ Test DELETE"""
        self.client.login(username="tester", password="12345")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ------------------- FILTERING / SEARCH / ORDER -------------------

    def test_filter_books_by_year(self):
        """✅ Test filtering by publication_year"""
        response = self.client.get(self.list_url, {"publication_year": 1997})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.book1.title)

    def test_search_books(self):
        """✅ Test search functionality"""
        response = self.client.get(self.list_url, {"search": "Chamber"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], self.book2.title)

    def test_order_books_by_year(self):
        """✅ Test ordering ascending"""
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            response.data[0]["publication_year"] <= response.data[1]["publication_year"]
        )
