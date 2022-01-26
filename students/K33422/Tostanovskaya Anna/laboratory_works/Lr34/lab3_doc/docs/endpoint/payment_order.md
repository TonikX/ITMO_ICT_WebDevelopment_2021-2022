# Описание эндпоинтов, связанных с моделью PaymentOrder

---
### Модель:
_models.py_
```
class PaymentOrder(models.Model):
    req = models.ForeignKey('Request', verbose_name='Заявка', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', verbose_name='Клиент', on_delete=models.CASCADE)
    invoice = models.ForeignKey('Invoice', verbose_name='Счет на оплату', on_delete=models.CASCADE)
    pay_date = models.DateField(verbose_name='Дата оплаты')
```

### Просмотр всех платежных поручений:
_serializer.py_
```
class PaymentOrderNestedSerializer(serializers.ModelSerializer):

    req = RequestWStatusViewSerializer()
    client = ClientViewSerializer()
    invoice = InvoiceViewSerializer()

    class Meta:
        model = PaymentOrder
        fields = "__all__"
```

_views.py_
```
class PaymentOrderListAPIView(generics.ListAPIView):
    queryset = PaymentOrder.objects.all()
    serializer_class = PaymentOrderNestedSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('paymentorder/', PaymentOrderListAPIView.as_view()),
    ...
]
```
---
### Создание платежного поручения:
_serializer.py_
```
class PaymentOrderCreateSerializer(serializers.Serializer):

    req = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())

    pay_date = serializers.DateField()

    def create(self, validated_data):
        payment_order = PaymentOrder(**validated_data)
        payment_order.save()
        return PaymentOrder(**validated_data)
```

_views.py_
```
class PaymentOrderCreateAPIView(generics.CreateAPIView):
    queryset = PaymentOrder.objects.all()
    serializer_class = PaymentOrderCreateSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('paymentorder/create/', PaymentOrderCreateAPIView.as_view()),
    ...
]
```
---
### Просмотр/изменение/удаление платежного поручения по id:
_serializer.py_
```
class PaymentOrderViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentOrder
        fields = "__all__"
```

_views.py_
```
class PaymentOrderRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentOrder.objects.all()
    serializer_class = PaymentOrderViewSerializer

```

_urls.py_
```
urlpatterns = [
    ...
    path('paymentorder/<int:pk>/', PaymentOrderRUDAPIView.as_view()),
    ...
]
```