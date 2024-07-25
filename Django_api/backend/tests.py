from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Category

class CategoryTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('categories')
        self.category_data = {'name': 'Test Category'}

    def test_get_category_list(self):
        # Create some test categories
        Category.objects.create(name='Category 1')
        Category.objects.create(name='Category 2')

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_valid_category(self):
        response = self.client.post(self.url, self.category_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'Test Category')

    def test_create_invalid_category(self):
        invalid_data = {'name': ''}  # Empty name should be invalid
        response = self.client.post(self.url, invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), 0)

    def test_create_duplicate_category(self):
        # Create a category first
        Category.objects.create(name='Test Category')

        # Try to create a category with the same name
        response = self.client.post(self.url, self.category_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), 1)
