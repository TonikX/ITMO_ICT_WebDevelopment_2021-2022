from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Topic(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Conference(models.Model):
    # конференция

    name = models.CharField("Название конференции", max_length=100)
    min_text = models.CharField("Небольшое описание", max_length=300)
    description = models.TextField("Большое описание", null=True)
    topics = models.ManyToManyField(Topic, verbose_name="Список тематик")
    location = models.CharField("Место проведения", max_length=30)
    description_location = models.CharField("Описание локации", max_length=30)
    # дата начала и конца
    date_start = models.DateTimeField(max_length=30)
    date_end = models.DateTimeField(max_length=30)
    # описание конференции
    description_conferences = models.CharField("Описание", max_length=100)
    keyword = models.CharField("Ключевые слова", max_length=50)
    # условия участия в конференции
    terms_participation = models.CharField("Условия участия", max_length=350)

    class Meta:
        verbose_name = 'Конференция'
        verbose_name_plural = 'Конференции'

    def __str__(self):
        return self.name


class Performance(models.Model):
    # выстулпение автора
    name = models.CharField("Тема выступления", max_length=40, default='')
    topics = models.ForeignKey(Topic, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.SET_NULL, null=True)
    result = models.BooleanField("Рекомендован к публикации", default=False)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Выступление'
        verbose_name_plural = 'Выступления'

    def __str__(self):
        return self.name


class Comments(models.Model):
    # комментарий

    # пользователь, написавший комментарий
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    # текст коментария
    text = models.TextField("Комментарий")
    # рейтинг поставленный коментатором
    rating = models.IntegerField("Рейтинг")

    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=False)
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return "{}".format(self.user)


