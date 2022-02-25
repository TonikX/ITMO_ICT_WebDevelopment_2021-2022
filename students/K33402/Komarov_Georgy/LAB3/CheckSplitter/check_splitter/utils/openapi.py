import re


def set_tags_description(result, generator, request, public):
    result['tags'] = [
        {'name': 'auth', 'description': 'Методы библиотеки авторизации'},
        {'name': 'checks', 'description': 'Методы для работы с чеками'},
        {'name': 'users', 'description': 'Методы для работы с аккаунтом текущего пользователя'},
    ]
    return result


def camelize_serializer_fields(result, generator, request, public):
    from djangorestframework_camel_case.util import camelize, camelize_re, underscore_to_camel

    components = generator.registry._components.values()
    for component in components:
        try:
            module = component.object.__module__
            # Ignore dj-rest-auth serializers for oauth2 compliance
            if module == 'dj_rest_auth.serializers':
                continue
        except:
            pass

        if 'properties' in component.schema:
            component.schema['properties'] = camelize(component.schema['properties'])
        if 'required' in component.schema:
            component.schema['required'] = [
                re.sub(camelize_re, underscore_to_camel, key) for key in component.schema['required']
            ]

    return result
