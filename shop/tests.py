from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from shop import views
from shop.models import Book, Category


# Create your tests here.
class TestBookStore(TestCase):
    """Tests for the bookstore app."""

    def setUp(self):
        self.client = Client()
        book = 

    def tearDown(self):
        pass

    def test_non_existing_book_search_by_name(self):
        """
        Test search functionality.

        Tests retrieval of a non existent book when user enters a book name.
        """
        url = reverse('search')
        data = {
            'name' = 'Django How to Code'
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            '<li>{0}</li>'.format(data.get('name')) in response.content
        )

    def test_existing_book_search_by_name(self):
        """
        Test search functionality.

        Tests retrieval of a book when user enters a book name.
        """
        url = reverse('search')
        data = {
            'name' = 'Django How to Code'
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            '<li>{0}</li>'.format(data.get('name')) in response.content
        )

    def test_search_by_category(self):
        """
        Test search functionality.

        Tests retrieval of a book when user enters a book category.
        """
        url = reverse('search')
        book_category = 'Programming'

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            '<li>{0}</li>'.format(data.get('name')) in response.content
        )