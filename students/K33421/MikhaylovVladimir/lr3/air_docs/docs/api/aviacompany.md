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
        "id": 1,
        "id_ekipazha": {
            "id": 1,
            "name": "Ввысь"
        },
        "id_workera": {
            "fio": "Косарев Сергей Владимирович",
            "age": 32,
            "education": "VSH",
            "stajh_raboty": 2,
            "passport": "1234567890"
        },
        "work": "Пилот"
    },
    {
        "id": 2,
        "id_ekipazha": {
            "id": 1,
            "name": "Ввысь"
        },
        "id_workera": {
            "fio": "Воздушный Антон Игоревич",
            "age": 39,
            "education": "VSH",
            "stajh_raboty": 5,
            "passport": "0000213432"
        },
        "work": "Второй Пилолт"
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
    "id_ekipazha": 1,
    "id_workera": 3,
    "work": "Пилот"
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
    "id": 3,
    "work": "Пилот",
    "id_ekipazha": 1,
    "id_workera": 3
}
```
