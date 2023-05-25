from django.test import TestCase
from .models import *
from django.urls import reverse
from rest_framework import status


class ServicesPLGetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ServicesPL.objects.create(
            service_type='у', title='some cool service', price=500)

    def test_get_service(self):
        url = reverse('ad_agency:service', args=['1'])
        data = {'id': 1, 'service_type': 'у',
                'title': 'some cool service', 'price': '500'}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)


class MaterialsPLGetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        MaterialsPL.objects.create(
            title='nice material', description='its very useful', price=300)

    def test_get_material(self):
        url = reverse('ad_agency:material', args=['1'])
        data = {'id': 1, 'title': 'nice material',
                'description': 'its very useful', 'price': '300'}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)


class ExecutorGetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Executor.objects.create(
            full_name='Timothee Chalamet', phone_num='89136662177')

    def test_get_executor(self):
        url = reverse('ad_agency:executor', args=['1'])
        data = {'id': 1, 'full_name': 'Timothee Chalamet',
                'phone_num': '89136662177'}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)
