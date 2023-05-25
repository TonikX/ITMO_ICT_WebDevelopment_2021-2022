from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import *


class ServicesPLUpdateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ServicesPL.objects.create(service_type='у', title='some cool service', price=500)

    def test_update_service(self):
        url = reverse('ad_agency:service', args=['1'])
        data = {'id': 1, 'service_type': 'у', 'title': 'some cool service', 'price': '500'}
        response_retrieve = self.client.get(url, format='json')
        self.assertEqual(response_retrieve.status_code, status.HTTP_200_OK)
        self.assertEqual(response_retrieve.json(), data)
        data['title'] = 'not so cool service'
        response_update = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_update.json(), data)


class MaterialsPLUpdateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        MaterialsPL.objects.create(title='nice material', description='its very useful', price=300)

    def test_update_material(self):
        url = reverse('ad_agency:material', args=['1'])
        data = {'id': 1, 'title': 'nice material', 'description': 'its very useful', 'price': '300'}
        response_retrieve = self.client.get(url, format='json')
        self.assertEqual(response_retrieve.status_code, status.HTTP_200_OK)
        self.assertEqual(response_retrieve.json(), data)
        data['price'] = '400'
        response_update = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_update.json(), data)


class ExecutorUpdateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Executor.objects.create(full_name='Timothee Chalamet', phone_num='89136662177')

    def test_update_executor(self):
        url = reverse('ad_agency:executor', args=['1'])
        data = {'id': 1, 'full_name': 'Timothee Chalamet', 'phone_num': '89136662177'}
        response_retrieve = self.client.get(url, format='json')
        self.assertEqual(response_retrieve.status_code, status.HTTP_200_OK)
        self.assertEqual(response_retrieve.json(), data)
        data['phone_num'] = '89136662169'
        response_update = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_update.json(), data)
