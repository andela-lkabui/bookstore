from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from shop import views
from shop.models import Book, Category


# Create your tests here.
class TestBookStore(TestCase):
    """Tests for the bookstore app."""

    def setUp(self):
        self.client = Client()
        self.category = Category(name="Programming")
        self.category.save()
        
    def tearDown(self):
        pass

    def test_non_existing_book_search_by_name(self):
        """
        Test search functionality.

        Tests retrieval of a non existent book when user enters a book name.
        """
        url = reverse('search')
        data = {
            'name_field': 'Django How to Code'
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            '<li>{0}</li>'.format(data.get('name')) in response.content,
            msg='Search by name should not return a book in the result'
        )

    def test_existing_book_search_by_name(self):
        """
        Test search functionality.

        Tests retrieval of a book when user enters a book name.
        """
        url = reverse('search')
        data = {
            'name_field': 'Django How to Code'
        }
        book = Book(category=self.category, name="Django How to Code")
        book.save()
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            '<li>{0}</li>'.format(data.get('name_field')) in response.content,
            msg='Search by name should return a book in the result'
        )

    def test_existing_book_search_by_category(self):
        """
        Test search functionality.

        Tests retrieval of a book when user enters a book category.
        """
        url = reverse('search')
        book_category = 'Programming'
        book = Book(category=self.category, name="Django How to Code")
        book.save()
        data = {
            'category_field': book.category.name
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            '<li>{0}</li>'.format(book.name) in response.content,
            msg='Search by category should return a book in the result'
        )

    def test_non_existing_book_search_by_category(self):
        """
        Test search functionality.

        Tests retrieval of non existent book when user enters a book category.
        """
        url = reverse('search')
        data = {
            'category_field': 'Programming'
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            '<li>{0}</li>'.format(data.get('category_field')) in response.content,
            msg='Search by category should not return a book in the result'
        )