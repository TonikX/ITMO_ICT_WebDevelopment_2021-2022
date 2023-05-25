from django.apps import AppConfig


class AdAgencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ad_agency'

    def ready(self):
        from . import signals
