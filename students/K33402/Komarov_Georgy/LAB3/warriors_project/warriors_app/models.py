from django.db import models


class Skill(models.Model):
    """
    Описание умений
    """

    class Meta:
        verbose_name = 'Умение'
        verbose_name_plural = 'Умения'

    title = models.CharField(max_length=120, unique=True, verbose_name='Наименование')

    def __str__(self):
        return self.title


class Profession(models.Model):
    """
    Описание профессии
    """

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    title = models.CharField(max_length=120, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')


class SkillOfWarrior(models.Model):
    """
    Описание умений война
    """

    class Meta:
        verbose_name = 'Умение воина'
        verbose_name_plural = 'Умение воинов'

    skill = models.ForeignKey('Skill', verbose_name='Умение', on_delete=models.CASCADE)
    warrior = models.ForeignKey('Warrior', verbose_name='Воин', on_delete=models.CASCADE)
    level = models.IntegerField(verbose_name='Уровень освоения умения')


class WarriorRaces(models.TextChoices):
    """
    Расы война
    """

    STUDENT = 'student', 'Студент'
    DEVELOPER = 'developer', 'Разработчик'
    TEAMLEAD = 'teamlead', 'Тимлид'


class Warrior(models.Model):
    """
    Описание война
    """

    class Meta:
        verbose_name = 'Воин'
        verbose_name_plural = 'Воины'

    race = models.CharField(max_length=10, choices=WarriorRaces.choices, verbose_name='Раса')
    name = models.CharField(max_length=120, verbose_name='Имя')
    level = models.IntegerField(default=0, verbose_name='Уровень')
    skills = models.ManyToManyField(Skill, through=SkillOfWarrior, related_name='warrior_skils', verbose_name='Умения')
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Профессия')
