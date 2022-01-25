# Таблица оценок

### Атрибуты таблицы:

 id ученика - models.ForeignKey(Student, on_delete=models.CASCADE)
 
 id предмета - models.ForeignKey(Subject, on_delete=models.CASCADE)
 
 Оценка - models.CharField(max_length=1, choices=(('1','1'), ('2','2'), ('3','3'),('4','4'), ('5','5')))

 Четверть - models.CharField(max_length=1, choices=(('1','1'), ('2','2'), ('3','3'),('4','4')))


