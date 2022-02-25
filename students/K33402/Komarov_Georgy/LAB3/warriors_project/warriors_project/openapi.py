from drf_spectacular.openapi import AutoSchema as DefaultAutoSchema


# DRF-spectacular custom schema inspector
class AutoSchema(DefaultAutoSchema):
    def get_tags(self):
        basename_tags_map = {
            'professions': ['professions'],
            'skills':      ['skills'],
            'warriors':    ['warriors'],
        }
        basename = getattr(self.view, 'basename', None)
        if basename in basename_tags_map:
            return basename_tags_map[basename]
        return super().get_tags()


def set_tags_description(result, generator, request, public):
    result['tags'] = [
        {'name': 'professions', 'description': 'Методы для работы с профессиями'},
        {'name': 'skills', 'description': 'Методы для работы с умениями'},
        {'name': 'warriors', 'description': 'Методы для работы с воинами'},
    ]
    return result
