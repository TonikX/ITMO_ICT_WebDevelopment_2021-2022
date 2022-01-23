# Таблица расписания

### Атрибуты:

id учителя - models.ForeignKey(Teacher, on_delete=models.CASCADE)

id кабинета - models.ForeignKey(Room, on_delete=models.CASCADE)

id предмета - models.ForeignKey(Subject, on_delete=models.CASCADE)

id класса - models.ForeignKey(StudentsGroup, on_delete=models.CASCADE, null=True)

День недели - models.CharField(max_length=30, choices=(('1','1'), ('2','2'), ('3','3'),('4','4'), ('5','5'), ('6','6')), default='1')

Номер урока - models.CharField(max_length=30, choices=(('1','1'), ('2','2'), ('3','3'),('4','4'), ('5','5'), ('6','6')), default='1')
