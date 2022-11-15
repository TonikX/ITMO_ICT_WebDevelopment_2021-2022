# Разрешение

Информация об эндпоинтах, связанных с разрешением управлять самолётом

## Cписок всех разрешений

**URL** : `/api/razrechenie/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "id_plane": {
            "id": 1,
            "type": "Боинг",
            "number": "737-500",
            "mesta": 167,
            "speed": 900,
            "avia": "Аэрофлот"
        },
        "id_ekipazha": {
            "id": 1,
            "name": "Красный"
        },
        "razrechenie": true
    },
    {
        "id": 2,
        "id_plane": {
            "id": 2,
            "type": "Боинг",
            "number": "747-8",
            "mesta": 450,
            "speed": 950,
            "avia": "Россия"
        },
        "id_ekipazha": {
            "id": 1,
            "name": "Красный"
        },
        "razrechenie": false
    },
    {
        "id": 3,
        "id_plane": {
            "id": 3,
            "type": "Airbus",
            "number": "A350",
            "mesta": 550,
            "speed": 935,
            "avia": "Аэрофлот"
        },
        "id_ekipazha": {
            "id": 3,
            "name": "Блестящий"
        },
        "razrechenie": true
    }
]
```
## Добавить новое разрешение для экипажа

**URL** : `/api/razrechenie/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id_plane": 7,
    "id_ekipazha": 7,
    "razrechenie": true
}
```

## Просмотр, изменение и удаление разрешений

**URL** : `api/razrechenie/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 6,
    "razrechenie": false,
    "id_plane": 7,
    "id_ekipazha": 7
}
```

