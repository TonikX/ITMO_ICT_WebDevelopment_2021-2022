from django.test import TestCase
from .models import *


class ServicesPLModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ServicesPL.objects.create(service_type='у', title='some cool service', price=500)

    def test_service_type_label(self):
        service = ServicesPL.objects.get(id=1)
        field_label = service._meta.get_field('service_type').verbose_name
        self.assertEquals(field_label, 'Вид услуги')


class MaterialsPLModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        MaterialsPL.objects.create(title='nice material', description='its very useful', price=300)

    def test_object_name_is_name(self):
        material = MaterialsPL.objects.get(id=1)
        expected_object_name = str(material.title)
        self.assertEquals(expected_object_name, str(material))


class ExecutorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Executor.objects.create(full_name='Timothee Chalamet', phone_num='89136662177')

    def test_full_name_max_length(self):
        executor = Executor.objects.get(id=1)
        max_length = executor._meta.get_field('full_name').max_length
        self.assertEquals(max_length, 50)
