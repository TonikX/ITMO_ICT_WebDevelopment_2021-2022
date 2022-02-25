from drf_spectacular.utils import extend_schema

profession_create_schema = extend_schema(summary='Создать профессию')
profession_retrieve_schema = extend_schema(summary='Получить профессию по ID')
profession_list_schema = extend_schema(summary='Список профессий')
profession_update_schema = extend_schema(summary='Редактировать профессию')
profession_delete_schema = extend_schema(summary='Удалить профессию')

skill_create_schema = extend_schema(summary='Создать умение')
skill_retrieve_schema = extend_schema(summary='Получить умение по ID')
skill_list_schema = extend_schema(summary='Список умений')
skill_update_schema = extend_schema(summary='Редактировать умение')
skill_delete_schema = extend_schema(summary='Удалить умение')

warrior_create_schema = extend_schema(summary='Создать воина')
warrior_retrieve_schema = extend_schema(summary='Получить воина по ID')
warrior_list_schema = extend_schema(summary='Список воинов')
warrior_update_schema = extend_schema(summary='Редактировать воина')
warrior_delete_schema = extend_schema(summary='Удалить воина')
