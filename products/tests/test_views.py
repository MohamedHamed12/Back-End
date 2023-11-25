from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from products.models import Category , Product
from products.serializers import CategorySerializer

class CategoryViewSetTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.category1 = Category.objects.create(name='Electronics', image='electronics.jpg')
        self.category2 = Category.objects.create(name='Clothing')
        self.url='/products/category/'
    def test_get_all_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_name(self):

        response = self.client.get('/products/category/', {'name__icontains': 'Electronics'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Electronics')

        response = self.client.get('/products/category/', {'name__icontains': 'Electronics'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Electronics')

    def test_create_category(self):
        data = {'name': 'Furniture'}
        response = self.client.post(self.url, data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        category = Category.objects.get(name='Furniture')
        self.assertEqual(category.name, 'Furniture')
    def test_update_category(self):
        data = {'name': 'Furniture_new'}
        response = self.client.put(f'/products/category/{self.category1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_delete_category(self):
        response = self.client.delete(f'/products/category/{self.category1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)






class ProductViewSetTests(TestCase):
    def setUp(self):
        # Create some test data
        self.category = Category.objects.create(name='Test Category1')
        self.product = Product.objects.create(name='Test Product1', price=20.0, strength=5, category=self.category)
        self.product = Product.objects.create(name='Test Product2', price=35.0, strength=5, category=self.category)
        self.product = Product.objects.create(name='Test Product3', price=25.0, strength=5, category=self.category)
        self.url = '/products/product/'  

    def test_list_products(self):
        response = self.client.get(self.url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3) 
    

    def test_create_product(self):
        data = {
            'name': 'New Product',
            'price': 30.0,
            'strength': 8,
            'category': self.category.id,
            'generic_name': 'Generic Name',
            'form': 'Form',
            'factory_company': 'Factory Company',
            'description': 'Description',
            
        }
        response = self.client.post(self.url, data, format='json') 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Product')
    def test_update_product(self):
        data = {
            'name': 'Updated Product',
            'price': 30.0,
            'strength': 8,
            'category': self.category.id,
            'generic_name': 'Generic Name',
            'form': 'Form',
            'factory_company': 'Factory Company',
            'description': 'Description',
            
        }
        response = self.client.put(f'/products/product/{self.product.id}/', data, content_type='application/json') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Product')
    def test_delete_product(self):
        response = self.client.delete(f'/products/product/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_by_name(self):

        response = self.client.get(self.url, {'name__icontains': 'Test Product1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Product1')
    def test_filter_by_price(self):

        response = self.client.get(self.url, {'price__gte': 20, 'price__lte': 30})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        prices=[item['price'] for item in response.data]
        self.assertEqual(max(prices)<=30, True)
        self.assertEqual(min(prices)>=20, True)
