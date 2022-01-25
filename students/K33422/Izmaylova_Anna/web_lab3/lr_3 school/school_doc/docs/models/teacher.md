# Таблица учителей

### Атрибуты:

Отчество - models.CharField(max_length=30)

id класса - models.ForeignKey(StudentsGroup, on_delete=models.CASCADE, null=True, blank=True)

id кабинета - models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
