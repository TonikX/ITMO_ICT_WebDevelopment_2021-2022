from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=ServicesPL)
def create_service(sender, instance, created, **kwargs):
    if created:
        print(f'Добавлена новая услуга: {instance.title}.')


@receiver(pre_save, sender=Client)
def update_client(sender, instance, **kwargs):
    if instance.id:
        current = Client.objects.get(id=instance.id)
        if instance.phone_num != current.phone_num:
            instance.old_phone = current.phone_num
            print(f'Обновлён номер телефона клиента "{instance.contact_person}": прошлый: {instance.old_phone}, '
                  f'актуальный: {instance.phone_num}.')
        else:
            print('Новый номер телефона совпадает с прошлым.')


@receiver(pre_delete, sender=ServicesPL)
def delete_service(sender, instance, **kwargs):
    with open('deleted_services.txt', 'a') as f:
        f.write(f'Услуга {instance.title} была удалена.')



