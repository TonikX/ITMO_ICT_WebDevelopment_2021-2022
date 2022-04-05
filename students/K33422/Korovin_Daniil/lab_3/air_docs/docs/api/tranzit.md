# Транзит

Информация об эндпоинтах, связанных с пересадкой на рейсах

## Cписок всех записей в "транзите"

**URL** : `/api/tranzit/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "weekday": "Monday",
        "time": "8:20",
        "room_number": "1",
        "group_number": "101",
        "teacher": "Boris Popov",
        "subject": "Chemistry"
    },
    {
        "id": 2,
        "weekday": "Friday",
        "time": "8:20",
        "room_number": "1",
        "group_number": "101",
        "teacher": "Boris Popov",
        "subject": "Chemistry"
    }
]
```
## Добавить новый пересадочный пункт

**URL** : `/api/tranzit/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "weekday": "2",
    "time": "4",
    "room_number": 5,
    "group_number": 1,
    "teacher": 6,
    "subject": 4
}
```

## Просмотр, изменение и удаление пересадки

**URL** : `api/tranzit/<int:pk>/`

**Method** : `POST`, `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 4,
    "weekday": "Wednesday",
    "time": "15:20",
    "room_number": "2",
    "group_number": "101",
    "teacher": "Valeria Pavlienko",
    "subject": "Sociology"
}
```

