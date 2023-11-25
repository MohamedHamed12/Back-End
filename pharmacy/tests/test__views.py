from django.test import TestCase
from django.urls import reverse
from products.models import Product, Category, Discount
from pharmacy.models import Pharmacy

class PharmacyViewSetTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.product = Product.objects.create(name="Test Product", price=10.0, strength=5, category=self.category)
        self.pharmacy = Pharmacy.objects.create(name="Test Pharmacy", phone="1234567890")

        self.url =reverse('pharmacy-list')

    def test_get_pharmacy(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Pharmacy')
    def test_create_pharmacy(self):
        data = {'name': 'Test Pharmacy', 'phone': '1234567890', 'location': 'Test Location'}
        response = self.client.post(self.url, data)
        # print(response.data)
        self.assertEqual(response.status_code, 201)
    def test_update_pharmacy(self):
        data = {'name': 'Updated Test Pharmacy', 'phone': '1234567890', 'location': 'Updated Test Location'}
        response = self.client.put(f'/pharmacy/pharmacy/{self.pharmacy.id}/', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Updated Test Pharmacy')