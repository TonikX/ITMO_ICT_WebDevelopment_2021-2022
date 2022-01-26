# Описание эндпоинтов, связанных с моделью Invoice

---
### Модель:
_models.py_
```
class Invoice(models.Model):
    req = models.ForeignKey('Request', verbose_name='Заявка', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', verbose_name='Клиент', on_delete=models.CASCADE)
    pay_due = models.DateField(verbose_name='Срок платежа')

    def __str__(self):
        return "{}-{}".format(self.id, self.client.legal_entity)
```

### Просмотр всех счетов на оплату (с возможностью фильтрации по legal_entity):
_serializer.py_
```
class InvoiceViewNestedSerializer(serializers.ModelSerializer):

    req = RequestWStatusViewSerializer()
    client = ClientViewSerializer()

    class Meta:
        model = Invoice
        fields = "__all__"
```

_views.py_
```
class InvoiceListAPIView(generics.ListAPIView):
    serializer_class = InvoiceViewNestedSerializer

    def get_queryset(self):
        queryset = Invoice.objects.all()
        params = self.request.query_params

        legal_entity = params.get('legal_entity', None)

        if legal_entity:
            queryset = queryset.filter(client__legal_entity=legal_entity)

        return queryset
```

_urls.py_
```
urlpatterns = [
    ...
    path('invoice/', InvoiceListAPIView.as_view()),
    ...
]
```
---
### Создание счета на оплату:
_serializer.py_
```
class InvoiceCreateSerializer(serializers.Serializer):

    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    req = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())

    pay_due = serializers.DateField()

    def create(self, validated_data):
        invoice = Invoice(**validated_data)
        invoice.save()
        return Invoice(**validated_data)
```

_views.py_
```
class InvoiceCreateAPIView(generics.CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceCreateSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('invoice/create/', InvoiceCreateAPIView.as_view()),
    ...
]
```
---
### Просмотр/изменение/удаление счета на оплату по id:
_serializer.py_
```
class InvoiceViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = "__all__"
```

_views.py_
```
class InvoiceRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceViewSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('invoice/<int:pk>/', InvoiceRUDAPIView.as_view()),
    ...
]
```