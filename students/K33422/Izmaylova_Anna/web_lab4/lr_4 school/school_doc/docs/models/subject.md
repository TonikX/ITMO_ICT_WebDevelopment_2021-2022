# Таблица предметов

### Атрибуты:

Название предмета - models.CharField(max_length=30)

id учителя - models.ForeignKey(Teacher, on_delete=models.CASCADE)

Статус предмета (базовый, профильный) - models.CharField(max_length=15, choices=(('basic','basic'), ('profile','profile')))