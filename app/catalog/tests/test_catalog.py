from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from catalog.models import Product


class ProductsListTest(APITestCase):
    """Тестирование списка продуктов /api/v1/catalog/products"""

    url = reverse('catalog:product-list')

    def setUp(self):
        """Создаем несколько продуктов"""

        self.client = APIClient()
        self.user = User.objects.create_user(username='user', password='password')
        self.client.force_login(self.user)

        self.count_products = 10
        for i in range(self.count_products):
            Product.objects.create(title=f'Product {i}',
                                   description=f'Description for product {i}',
                                   price=f'10{i}.{i}')

    def test_status_ok(self):
        """Делаем запрос и проверяем статус код"""

        request = self.client.get(self.url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request.data), self.count_products)

    def test_create_product(self):
        """Успешное создание продукта"""

        data = {
            'title': 'Новый продукт',
            'description': 'Описание нового продукта',
            'price': "100.99"
        }

        request = self.client.post(self.url, data, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.last().title, data.get('title'))

    def test_create_product_error_empty_name(self):
        """Ошибка при создании продукта с пустым названием"""

        data = {
            'title': ' ',
            'description': 'Описание продукта',
            'price': "100.99"
        }

        request = self.client.post(self.url, data, format='json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_error_price(self):
        """Ошибка при создании продукта с отрицательной ценой"""

        data = {
            'title': 'Новый продукт',
            'description': 'Описание продукта',
            'price': "-1"
        }

        request = self.client.post(self.url, data, format='json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)