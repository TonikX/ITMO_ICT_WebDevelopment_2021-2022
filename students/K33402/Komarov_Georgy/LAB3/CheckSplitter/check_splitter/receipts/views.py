from decimal import Decimal
from urllib.parse import parse_qs

import requests
from django.conf import settings
from djangorestframework_camel_case.parser import CamelCaseJSONParser
from drf_spectacular.utils import extend_schema_view
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from receipts.models import Receipt, ReceiptItem, ReceiptItemPart
from receipts.openapi import *
from receipts.serializers import CheckSerializer, CheckItemPartSerializer
from utils.views import CamelCaseView


@extend_schema_view(
    list=checks_list_schema,
    retrieve=checks_retrieve_schema,
    sync=checks_sync_schema,
    items=checks_items_schema,
)
class CheckViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet, CamelCaseView):
    serializer_class = CheckSerializer
    queryset = Receipt.objects.all()
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)

    @action(detail=False, methods=['POST'], serializer_class=serializers.Serializer)
    def sync(self, request, *args, **kwargs):
        token = self.request.user.check_scan_token
        if not token:
            raise ValidationError({'detail': 'Невалидный токен ЧекСкан'})

        checks_list_url = settings.CHECKSCAN_API_URL + '/receipts/filtered'
        params = {
            'limit': 25,
            'skip':  0,
        }
        headers = {
            'Accept':        'application/json',
            'User-Agent':    'okhttp/4.9.0',
            'Os':            'android',
            'App-Version':   '1.48.0.6',
            'Test-Group-Id': '0',
        }
        cookies = {'remember-me': token}

        try:
            checks_data = requests.post(checks_list_url, params=params, headers=headers, cookies=cookies, json={})
            receipts_data = checks_data.json()['receipts']

            for receipt_data in receipts_data:
                qr_code = receipt_data.get('qr_code')
                qr_params = parse_qs(qr_code) if qr_code else {}
                fn_list = qr_params.get('fn')
                fp_list = qr_params.get('fp')
                fd_list = qr_params.get('i')

                shop = receipt_data.get('shop')
                if shop:
                    city = shop.get('city', '')
                    street = shop.get('street', '')
                    building = shop.get('build', '')
                    address = ' '.join(filter(str.strip, [city, street, building]))
                else:
                    address = None

                reciept, _ = Receipt.objects.get_or_create(
                    id=receipt_data['id'],
                    defaults={
                        'qr_data':     receipt_data['qr_code'],
                        'name':        shop.get('name') if shop else '',
                        'address':     address,
                        'date':        receipt_data['purchaseDateTime'],
                        'total_sum':   receipt_data['totalSum'],
                        'fn':          fn_list[0] if fn_list else None,
                        'fp':          fp_list[0] if fp_list else None,
                        'fd':          fd_list[0] if fd_list else None,
                        'org_inn':     receipt_data['inn'],
                        'org_name':    receipt_data['user'],
                        'org_address': receipt_data.get('retailPlaceAddress'),
                    },
                )

                receipt_items_data = receipt_data['items']
                for receipt_item_data in receipt_items_data:
                    ReceiptItem.objects.get_or_create(
                        id=receipt_item_data['id'],
                        defaults={
                            'receipt':  reciept,
                            'name':     receipt_item_data['name'],
                            'price':    receipt_item_data['price'],
                            'quantity': Decimal(receipt_item_data['quantity']),
                            'sum':      receipt_item_data['sum'],
                        },
                    )

        except:
            raise ValidationError({'detail': 'Ошибка взаимодействия с внешним API'})

        return Response(status=200)

    @action(detail=True, methods=['PUT'], serializer_class=CheckItemPartSerializer, parser_classes=[CamelCaseJSONParser])
    def items(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(many=True, data=request.data)
        serializer.is_valid(raise_exception=True)

        ReceiptItemPart.objects.filter(item__receipt=instance).delete()
        serializer.save()
        return Response(status=200)
