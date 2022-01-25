# Таблица класса

### Атрибуты:

id ученика - models.ForeignKey(Student, on_delete=models.CASCADE)

id названия класса - models.ForeignKey(Groups, on_delete=models.CASCADE, null=True)

