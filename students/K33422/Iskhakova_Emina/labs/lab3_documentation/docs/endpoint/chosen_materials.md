# Описание эндпоинтов, связанных с моделью ChosenMaterials

---
### Модель:
_models.py_
```
class ChosenMaterials(models.Model):
    material = models.ForeignKey('MaterialsPL', verbose_name='Выбранный материал', on_delete=models.CASCADE)
    req = models.ForeignKey('Request', verbose_name='Заявка', on_delete=models.CASCADE)
    total_cost = models.CharField(max_length=30, verbose_name='Общая стоимость материалов')
    amount = models.IntegerField(verbose_name='Количество материалов(шт.)')
```

### Просмотр всех выбранных материалов (с возможностью фильтрации по _req_):
_serializer.py_
```
class ChosenMaterialWMRsViewSerializer(serializers.ModelSerializer):

    material = serializers.StringRelatedField(read_only=True)
    req = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ChosenMaterials
        fields = "__all__"
```

_views.py_
```
class ChosenMaterialsListAPIView(generics.ListAPIView):
    serializer_class = ChosenMaterialWMRsViewSerializer

    def get_queryset(self):
        queryset = ChosenMaterials.objects.all()
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
    path('chosenmaterials/', ChosenMaterialsListAPIView.as_view()),
    ...
]
```
---
### Создание выбранных материалов:
_serializer.py_
```
class ChosenMaterialsCreateSerializer(serializers.Serializer):

    material = serializers.PrimaryKeyRelatedField(queryset=MaterialsPL.objects.all())
    req = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())

    total_cost = serializers.CharField(max_length=30)
    amount = serializers.IntegerField()

    def create(self, validated_data):
        chosen_materials = ChosenMaterials(**validated_data)
        chosen_materials.save()
        return ChosenMaterials(**validated_data)
```

_views.py_
```
class ChosenMaterialsCreateAPIView(generics.CreateAPIView):
    queryset = ChosenMaterials.objects.all()
    serializer_class = ChosenMaterialsCreateSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('chosenmaterials/create/', ChosenMaterialsCreateAPIView.as_view()),
    ...
]
```
---
### Просмотр/изменение/удаление выбранных материалов по id:
_serializer.py_
```
class ChosenMaterialsViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChosenMaterials
        fields = "__all__"
```

_views.py_
```
class ChosenMaterialsRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChosenMaterials.objects.all()
    serializer_class = ChosenMaterialsViewSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('chosenmaterials/<int:pk>/', ChosenMaterialsRUDAPIView.as_view()),
    ...
]
```
### Просмотр всех выбранных материалов с вложенными сериализаторами:
_serializer.py_
```
class ChosenMaterialsNestedSerializer(serializers.ModelSerializer):

    req = RequestNestedSerializer()
    material = MaterialsPLViewSerializer()

    class Meta:
        model = ChosenMaterials
        fields = "__all__"
```

_views.py_
```
class ChosenMaterialsFullListAPIView(generics.ListAPIView):
    queryset = ChosenMaterials.objects.all()
    serializer_class = ChosenMaterialsNestedSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('chosenmaterials/full/', ChosenMaterialsFullListAPIView.as_view()),
    ...
]
```