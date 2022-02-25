from django.db import models
from django.db.models import UniqueConstraint

from users.models import User
from utils.models import ExtendedModel


class Receipt(ExtendedModel):
    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'

    id = models.PositiveBigIntegerField(primary_key=True, verbose_name='ID чека')
    qr_data = models.CharField(max_length=100, null=True, blank=True, verbose_name='Данные QR кода')
    name = models.CharField(max_length=1000, verbose_name='Наименование')
    address = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Адрес')
    date = models.DateTimeField(verbose_name='Дата покупки')
    total_sum = models.PositiveIntegerField(verbose_name='Сумма чека')
    fn = models.CharField(max_length=20, null=True, blank=True, verbose_name='ФН', help_text='Номер фискального накопителя')
    fp = models.CharField(max_length=20, null=True, blank=True, verbose_name='ФПД', help_text='Фискальный признак документа')
    fd = models.CharField(max_length=20, null=True, blank=True, verbose_name='ФД', help_text='Номер фискального документа')
    org_inn = models.CharField(max_length=20, verbose_name='ИНН организации')
    org_name = models.CharField(max_length=20, verbose_name='Название организации')
    org_address = models.CharField(max_length=20, null=True, blank=True, verbose_name='Юр. адрес организации')
    users = models.ManyToManyField(User, related_name='receipts', verbose_name='Пользователи')

    def __str__(self):
        return f'[{self.pk}] {self.name} ({self.date})'


class ReceiptItem(ExtendedModel):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, related_name='items', verbose_name='Чек')
    id = models.PositiveBigIntegerField(primary_key=True, verbose_name='ID товара')
    name = models.CharField(max_length=1000, verbose_name='Наименование')
    price = models.PositiveIntegerField(verbose_name='Цена')
    quantity = models.DecimalField(decimal_places=10, max_digits=15, verbose_name='Количество')
    sum = models.PositiveIntegerField(verbose_name='Сумма')
    parts = models.ManyToManyField(User, through='ReceiptItemPart', verbose_name='Пользователи')

    def __str__(self):
        return f'[{self.pk}] {self.name}'


class ReceiptItemPart(models.Model):
    class Meta:
        verbose_name = 'Товар - пользователь: количество'
        verbose_name_plural = 'Товары - пользователи: количество'
        constraints = [UniqueConstraint(fields=('user', 'item'), name='uq_user_item')]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    item = models.ForeignKey(ReceiptItem, on_delete=models.CASCADE, verbose_name='Товар')
    part = models.DecimalField(decimal_places=10, max_digits=15, verbose_name='Количество')
