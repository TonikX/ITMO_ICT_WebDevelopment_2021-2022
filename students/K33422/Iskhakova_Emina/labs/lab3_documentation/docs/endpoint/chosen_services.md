# Описание эндпоинтов, связанных с моделью ChosenServices

---
### Модель:
_models.py_
```
class ChosenServices(models.Model):
    service = models.ForeignKey('ServicesPL', verbose_name='Выбранная услуга', on_delete=models.CASCADE)
    req = models.ForeignKey('Request', verbose_name='Заявка', on_delete=models.CASCADE)
    total_cost = models.CharField(max_length=30, verbose_name='Общая стоимость услуг')
```

### Просмотр всех выбранных сервисов (с возможностью фильтрации по _req_):
_serializer.py_
```
class ChosenServicesWSRViewSerializer(serializers.ModelSerializer):

    service = serializers.StringRelatedField(read_only=True)
    req = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ChosenServices
        fields = "__all__"
```

_views.py_
```
class ChosenServicesListAPIView(generics.ListAPIView):
    serializer_class = ChosenServicesWSRViewSerializer

    def get_queryset(self):
        queryset = ChosenServices.objects.all()
        params = self.request.query_params

        req = params.get('req', None)

        if req:
            queryset = queryset.filter(req=req)

        return queryset
```

_urls.py_
```
urlpatterns = [
    ...
    path('chosenservices/', ChosenServicesListAPIView.as_view()),
    ...
]
```
---
### Создание выбранных сервисов:
_serializer.py_
```
class ChosenServicesCreateSerializer(serializers.Serializer):

    service = serializers.PrimaryKeyRelatedField(queryset=ServicesPL.objects.all())
    req = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())
    total_cost = serializers.CharField(max_length=30)

    def create(self, validated_data):
        chosen_services = ChosenServices(**validated_data)
        chosen_services.save()
        return ChosenServices(**validated_data)
```

_views.py_
```
class ChosenServicesCreateAPIView(generics.CreateAPIView):
    queryset = ChosenServices.objects.all()
    serializer_class = ChosenServicesCreateSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('chosenservices/create/', ChosenServicesCreateAPIView.as_view()),
    ...
]
```
---
### Просмотр/изменение/удаление выбранных сервисов по id:
_serializer.py_
```
class ChosenServicesViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChosenServices
        fields = "__all__"
```

_views.py_
```
class ChosenServicesRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChosenServices.objects.all()
    serializer_class = ChosenServicesViewSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('chosenservices/<int:pk>/', ChosenServicesRUDAPIView.as_view()),
    ...
]
```
### Просмотр всех выбранных сервисов с вложенными сериализаторами:
_serializer.py_
```
class ChosenServicesNestedSerializer(serializers.ModelSerializer):

    req = RequestNestedSerializer()
    service = ServicesPLWTypeViewSerializer()

    class Meta:
        model = ChosenServices
        fields = "__all__"
```

_views.py_
```
class ChosenServicesFullListAPIView(generics.ListAPIView):
    queryset = ChosenServices.objects.all()
    serializer_class = ChosenServicesNestedSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('chosenservices/full/', ChosenServicesFullListAPIView.as_view()),
    ...
]
```