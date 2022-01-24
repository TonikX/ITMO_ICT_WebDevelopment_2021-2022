import os
from hashlib import md5
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from utils.models import ExtendedModel


def avatar_upload_path(instance, filename):
    file_name, file_extension = os.path.splitext(filename)

    return f'avatars/{instance.username}/{uuid4()}{file_extension}'


class User(ExtendedModel, AbstractUser):
    class Meta:
        verbose_name = 'Пользователь CheckSplitter'
        verbose_name_plural = 'Пользователи CheckSplitter'

    email = models.EmailField(unique=True, verbose_name='E-Mail')
    avatar = ProcessedImageField(upload_to=avatar_upload_path, null=True, blank=True, verbose_name='Аватар',
                                 processors=[ResizeToFill(300, 300, upscale=True)],
                                 format='JPEG',
                                 options={'quality': 60})
    check_scan_token = models.TextField(null=True, blank=True, verbose_name='Токен ЧекСкан')

    @property
    @extend_schema_field(OpenApiTypes.URI)
    def avatar_url(self) -> str:
        return self.avatar if self.avatar else f'https://www.gravatar.com/avatar/{md5(self.email.lower().strip().encode()).hexdigest()}?d=identicon'

    @property
    def full_name(self) -> str:
        return f'{self.last_name} {self.first_name}'.strip()
