# Описание эндпоинтов, связанных с моделью WorkGroup

---
### Модель:
_models.py_
```
class WorkGroup(models.Model):
    req = models.ForeignKey('Request', verbose_name='Заявка', on_delete=models.CASCADE)
    executor = models.ForeignKey('Executor', verbose_name='Исполнитель', on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name='Дата начала работы')
    end_date = models.DateField(verbose_name='Дата окончания работы')
```

### Просмотр всех рабочих групп (с возможностью фильтрации по _req, executor, start_date, end_date_):
_serializer.py_
```
class WorkGroupWREViewSerializer(serializers.ModelSerializer):

    req = serializers.StringRelatedField(read_only=True)
    executor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = WorkGroup
        fields = "__all__"
```

_views.py_
```
class WorkGroupListAPIView(generics.ListAPIView):
    serializer_class = WorkGroupWREViewSerializer

    def get_queryset(self):
        queryset = WorkGroup.objects.all()
        params = self.request.query_params

        req = params.get('req', None)
        executor = params.get('executor', None)
        start_date = params.get('start_date', None)
        end_date = params.get('end_date', None)

        if req:
            queryset = queryset.filter(req=req)

        if executor:
            queryset = queryset.filter(executor=executor)

        if start_date:
            queryset = queryset.filter(start_date__gte=start_date)

        if end_date:
            queryset = queryset.filter(end_date__lte=end_date)

        return queryset
```

_urls.py_
```
urlpatterns = [
    ...
    path('workgroup/', WorkGroupListAPIView.as_view()),
    ...
]
```
---
### Создание рабочей группы:
_serializer.py_
```
class WorkGroupCreateSerializer(serializers.Serializer):

    executor = serializers.PrimaryKeyRelatedField(queryset=Executor.objects.all())
    req = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())

    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def create(self, validated_data):
        work_group = WorkGroup(**validated_data)
        work_group.save()
        return WorkGroup(**validated_data)
```

_views.py_
```
class WorkGroupCreateAPIView(generics.CreateAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupCreateSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('workgroup/create/', WorkGroupCreateAPIView.as_view()),
    ...
]
```
---
### Просмотр/изменение/удаление рабочей группы по id:
_serializer.py_
```
class WorkGroupViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkGroup
        fields = "__all__"
```

_views.py_
```
class WorkGroupRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupViewSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('workgroup/<int:pk>/', WorkGroupRUDAPIView.as_view()),
    ...
]
```
### Просмотр всех рабочих групп с вложенными сериализаторами:
_serializer.py_
```
class WorkGroupNestedSerializer(serializers.ModelSerializer):

    req = RequestNestedSerializer()
    executor = ExecutorViewSerializer()

    class Meta:
        model = WorkGroup
        fields = "__all__"
```

_views.py_
```
class WorkGroupFullListAPIView(generics.ListAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupNestedSerializer
```

_urls.py_
```
urlpatterns = [
    ...
    path('workgroup/full/', WorkGroupFullListAPIView.as_view()),
    ...
]
```