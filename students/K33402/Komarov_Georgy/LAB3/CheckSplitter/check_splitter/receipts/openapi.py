from drf_spectacular.utils import extend_schema

from receipts.serializers import CheckItemPartSerializer, CheckSerializer

checks_list_schema = extend_schema(summary='Получить список чеков')
checks_retrieve_schema = extend_schema(summary='Получить чек по ID')
checks_sync_schema = extend_schema(summary='Синхронизировать чеки из ЧекСкан')
checks_items_schema = extend_schema(summary='Установить взаиморасчет для чека',
                                    request=CheckItemPartSerializer(many=True),
                                    responses={200: ''})
checks_users_schema = extend_schema(summary='Изменить пользователей в чеке', responses={200: CheckSerializer})
checks_name_schema = extend_schema(summary='Изменить название чека')
