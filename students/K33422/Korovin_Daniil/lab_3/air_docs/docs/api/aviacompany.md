# Авиакомпания
Информация об эндпоинтах, связанных с занимаемыми должностями
сотрудников компании.

## Cписок всех записей в журнале авиакомпании

**URL** : `/api/aviacompany/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 2,
        "id_ekipazha": {
            "id": 1,
            "name": "Красный"
        },
        "id_workera": {
            "fio": "Янов Филипп Андреевич",
            "age": 20,
            "education": "VSN",
            "stajh_raboty": 1,
            "passport": "3424342453"
        },
        "work": "Главный стюард"
    },
    {
        "id": 5,
        "id_ekipazha": {
            "id": 3,
            "name": "Блестящий"
        },
        "id_workera": {
            "fio": "Лодырев Александр Сергеевич",
            "age": 54,
            "education": "VSH",
            "stajh_raboty": 26,
            "passport": "2456111334"
        },
        "work": "Штурман"
    }
]
```
## Добавить нового сотрудника в экипаж с определением должности

**URL** : `/api/aviacompany/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id_ekipazha": 7,
    "id_workera": 10,
    "work": "Штурман"
}
```

## Просмотр, изменение и удаление с должности

**URL** : `api/aviacompany/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 6,
    "work": "Помощник штурмана",
    "id_ekipazha": 7,
    "id_workera": 10
}
```

