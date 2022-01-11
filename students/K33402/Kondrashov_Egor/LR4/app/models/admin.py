from fastapi_admin.models import AbstractAdmin


class Admin(AbstractAdmin):
    """
    Модель админки для входа в FastAPI admin
    (использует username и password)
    """
