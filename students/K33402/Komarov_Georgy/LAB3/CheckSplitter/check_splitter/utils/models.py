import warnings

from django.db import models
from django_currentuser.db.models import CurrentUserField
from simple_history.models import HistoricalRecords

warnings.filterwarnings('ignore', message='You passed an argument to CurrentUserField that will be ignored. Avoid args and '
                                          'following kwargs: default, null, to.')


class ExtendedModel(models.Model):
    class Meta:
        abstract = True

    created_by = CurrentUserField(
        verbose_name='Кем создан',
        editable=False,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_created',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        editable=False,
        auto_now_add=True,
    )
    updated_by = CurrentUserField(
        on_update=True,
        verbose_name='Кем обновлён',
        editable=False,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_updated',
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        editable=False,
        auto_now=True,
    )
    history = HistoricalRecords(
        verbose_name='История изменений',
        inherit=True,
    )

    @property
    def _history_user(self):
        return self.updated_by

    @_history_user.setter
    def _history_user(self, value):
        self.updated_by = value
