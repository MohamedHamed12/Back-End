from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from products.models import Product

# class ProductViewSetTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.product1 = Product.objects.create(name='Product1', price=50, category='Electronics')
#         self.product2 = Product.objects.create(name='Product2', price=30, category='Clothing')

#     def test_get_all_products(self):
#         response = self.client.get('/products/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 2)

#     def test_filter_by_name(self):
#         response = self.client.get('/products/', {'name': 'Product1'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]['name'], 'Product1')

#     def test_filter_by_price(self):
#         response = self.client.get('/products/', {'price': 30})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]['price'], '30.00')

    # Add more tests for other filters as needed
