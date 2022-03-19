# Описание эндпоинтов, связанных с моделью ServicesPL

---

### Модель:
_models.py_
```
class ServicesPL(models.Model):

    service_types = (
        ('у', 'уличная реклама'),
        ('и', 'реклама в интерьере внутри помещения'),
        ('т', 'реклама на транспортных средствах'),
        ('п', 'печатная реклама'),
    )

    service_type = models.CharField(max_length=20, choices=service_types, verbose_name='Вид услуги')
    title = models.CharField(max_length=50, verbose_name='Наименование услуги')
    price = models.CharField(max_length=30, verbose_name='Стоимость услуги')

    def __str__(self):
        return self.title
```

### Просмотр всех сервисов(с возможностью фильтрации по service_type):
_serializer.py_
```
class ServicesPLWTypeViewSerializer(serializers.ModelSerializer):

    service_type = serializers.CharField(source="get_service_type_display", read_only=True)

    class Meta:
        model = ServicesPL
        fields = "__all__"

```

_views.py_
```
class ServicesPLListAPIView(generics.ListAPIView):
    serializer_class = ServicesPLWTypeViewSerializer

    def get_queryset(self):
        queryset = ServicesPL.objects.all()
        params = self.request.query_params

        service_type = params.get('service_type', None)

        if service_type:
            queryset = queryset.filter(service_type=service_type)

        return queryset
```

_urls.py_
```
urlpatterns = [
    ...
    path('servicespl/', ServicesPLListAPIView.as_view()),
    ...
]
```
---
### Создание сервиса:
_serializer.py_
```
class ServicesPLCreateSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=50)
    price = serializers.CharField(max_length=30)
    service_type = serializers.ChoiceField(choices=ServicesPL.service_types)

    def create(self, validated_data):
        services_pl = ServicesPL(**validated_data)
        services_pl.save()
        return ServicesPL(**validated_data)
```

_views.py_
```
class ServicesPLCreateAPIView(generics.CreateAPIView):
    queryset = ServicesPL.objects.all()
    serializer_class = ServicesPLCreateSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('servicespl/create/', ServicesPLCreateAPIView.as_view()),
    ...
]
```
---
### Просмотр/изменение/удаление сервиса по id:
_serializer.py_
```
class ServicesPLViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicesPL
        fields = "__all__"

```

_views.py_
```
class ServicesPLRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicesPL.objects.all()
    serializer_class = ServicesPLViewSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('servicespl/<int:pk>/', ServicesPLRUDAPIView.as_view()),
    ...
]
```