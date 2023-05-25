from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import *


class ServicesPLCreateTest(TestCase):
    def test_create_service(self):
        url = reverse('ad_agency:service-create')
        data = {'service_type': 'у', 'title': 'some cool service', 'price': '500'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)


class MaterialsPLCreateTest(TestCase):
    def test_create_material(self):
        url = reverse('ad_agency:material-create')
        data = {'title': 'nice material', 'description': 'its very useful', 'price': '300'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)


class ExecutorCreateTest(TestCase):
    def test_create_executor(self):
        url = reverse('ad_agency:executor-create')
        data = {'full_name': 'Timothee Chalamet', 'phone_num': '89136662177'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)
