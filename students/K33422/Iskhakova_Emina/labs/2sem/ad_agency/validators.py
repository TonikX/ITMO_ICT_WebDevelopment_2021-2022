from django.core.exceptions import ValidationError
import magic


def validate_file_size(file_upload):
    if file_upload.size > 1024 * 1024:
        raise ValidationError('Файл слишком большой.')


def validate_file_type(file_upload):
    file_type = magic.from_buffer(file_upload.read(), mime=True)
    if file_type not in ('image/png', 'image/jpeg', 'image/jpg'):
        raise ValidationError('Загрузите, пожалуйста, картинку в формате PNG или JPG.')
