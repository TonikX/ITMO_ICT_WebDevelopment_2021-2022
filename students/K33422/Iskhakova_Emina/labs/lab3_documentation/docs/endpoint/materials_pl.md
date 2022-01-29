# Описание эндпоинтов, связанных с моделью MaterialsPL

---

### Модель:
_models.py_
```
class MaterialsPL(models.Model):

    title = models.CharField(max_length=50, verbose_name='Наименование материала')
    description = models.CharField(max_length=150, verbose_name='Характеристики')
    price = models.CharField(max_length=30, verbose_name='Цена')

    def __str__(self):
        return self.title
```

### Просмотр всех материалов:
_serializer.py_
```
class MaterialsPLViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialsPL
        fields = "__all__"
```

_views.py_
```
class MaterialsPLListAPIView(generics.ListAPIView):
    queryset = MaterialsPL.objects.all()
    serializer_class = MaterialsPLViewSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('materialspl/', MaterialsPLListAPIView.as_view()),
    ...
]
```
---
### Создание материала:
_serializer.py_
```
class MaterialsPLCreateSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=150)
    price = serializers.CharField(max_length=30)

    def create(self, validated_data):
        materials_pl = MaterialsPL(**validated_data)
        materials_pl.save()
        return MaterialsPL(**validated_data)
```

_views.py_
```
class MaterialsPLCreateAPIView(generics.CreateAPIView):
    queryset = MaterialsPL.objects.all()
    serializer_class = MaterialsPLCreateSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('materialspl/create/', MaterialsPLCreateAPIView.as_view()),
    ...
]
```
---
### Просмотр/изменение/удаление материала по id:
_serializer.py_
```
class MaterialsPLViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialsPL
        fields = "__all__"
```

_views.py_
```
class MaterialsPLRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaterialsPL.objects.all()
    serializer_class = MaterialsPLViewSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('materialspl/<int:pk>/', MaterialsPLRUDAPIView.as_view()),
    ...
]
```