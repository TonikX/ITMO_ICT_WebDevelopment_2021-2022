# Описание эндпоинтов, связанных с моделью Request

---
### Модель:
_models.py_
```
class Request(models.Model):

    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Заказчик')
    req_date = models.DateField(verbose_name='Дата заявки')
    workload = models.CharField(max_length=30, verbose_name='Объем работ')
    final_price = models.CharField(max_length=30, verbose_name='Итоговая стоимость')
    status_types = (
        ('н', 'не оплачено'),
        ('о', 'оплачено'),
    )
    status = models.CharField(max_length=20, choices=status_types, verbose_name='Состояние')

    def __str__(self):
        return "{}-{}-{}".format(self.id, self.client.legal_entity, self.req_date)
```

### Просмотр всех заявок( с возможностью фильтрации по _status, from_date, to_date, legal_entity_):
_serializer.py_
```
class RequestWStatusViewSerializer(serializers.ModelSerializer):

    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Request
        fields = "__all__"
```

_views.py_
```
class RequestListAPIView(generics.ListAPIView):
    serializer_class = RequestWStatusViewSerializer

    def get_queryset(self):
        queryset = Request.objects.all()
        params = self.request.query_params

        status = params.get('status', None)
        from_date = params.get('from_date', None)
        to_date = params.get('to_date', None)
        legal_entity = params.get('legal_entity', None)

        if status:
            queryset = queryset.filter(status=status)

        if from_date:
            queryset = queryset.filter(req_date__gte=from_date)

        if to_date:
            queryset = queryset.filter(req_date__lte=to_date)

        if legal_entity:
            queryset = queryset.filter(client__legal_entity=legal_entity)

        return queryset
```

_urls.py_
```
urlpatterns = [
    ...
    path('request/', RequestListAPIView.as_view()),
    ...
]
```
---
### Создание заявки:
_serializer.py_
```
class RequestCreateSerializer(serializers.Serializer):

    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    req_date = serializers.DateField()
    workload = serializers.CharField(max_length=30)
    final_price = serializers.CharField(max_length=30)
    status = serializers.ChoiceField(choices=Request.status_types)

    def create(self, validated_data):
        request = Request(**validated_data)
        request.save()
        return Request(**validated_data)
```

_views.py_
```
class RequestCreateAPIView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestCreateSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('request/create/', RequestCreateAPIView.as_view()),
    ...
]
```
---
### Просмотр/изменение/удаление заявки по id:
_serializer.py_
```
class RequestViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = "__all__"
```

_views.py_
```
class RequestRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestViewSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('request/<int:pk>/', RequestRUDAPIView.as_view()),
    ...
]
```
### Просмотр заявок с вложенными сериализаторами:
_serializer.py_
```
class RequestNestedSerializer(serializers.ModelSerializer):

    client = ClientViewSerializer()
    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Request
        fields = "__all__"
```

_views.py_
```
class RequestNestedAPIView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestNestedSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('request/nested/', RequestNestedAPIView.as_view()),
    ...
]
```