# Описание эндпоинтов, связанных с моделью Executor

---
### Модель:
_models.py_
```
class Executor(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='ФИО')
    phone_num = models.CharField(max_length=12, verbose_name='Номер телефона')

    def __str__(self):
        return self.full_name
```

### Просмотр всех исполнителей:
_serializer.py_
```
class ExecutorViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Executor
        fields = "__all__"
```

_views.py_
```
class ExecutorListAPIView(generics.ListAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorViewSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('executor/', ExecutorListAPIView.as_view()),
    ...
]
```
---
### Создание исполнителя:
_serializer.py_
```
class ExecutorCreateSerializer(serializers.Serializer):

    full_name = serializers.CharField(max_length=50)
    phone_num = serializers.CharField(max_length=12)

    def create(self, validated_data):
        executor = Executor(**validated_data)
        executor.save()
        return Executor(**validated_data)
```

_views.py_
```
class ExecutorCreateAPIView(generics.CreateAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorCreateSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('executor/create/', ExecutorCreateAPIView.as_view()),
    ...
]
```
---
### Просмотр/изменение/удаление исполнителя по id:
_serializer.py_
```
class ExecutorViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Executor
        fields = "__all__"
```

_views.py_
```
class ExecutorRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorViewSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('executor/<int:pk>/', ExecutorRUDAPIView.as_view()),
    ...
]
```