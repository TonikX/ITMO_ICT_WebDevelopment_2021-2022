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
            "type": "Boing",
            "number": "10-20",
            "mesta": 600,
            "speed": 850,
            "avia": "Россфлот"
        },
        "id_ekipazha": {
            "id": 1,
            "name": "Ввысь"
        },
        "razrechenie": true
    },
    {
        "id": 2,
        "id_plane": {
            "id": 2,
            "type": "Boing",
            "number": "20-20",
            "mesta": 200,
            "speed": 900,
            "avia": "Россфлот"
        },
        "id_ekipazha": {
            "id": 2,
            "name": "Старт"
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
    "id_plane": 3,
    "id_ekipazha": 3,
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
    "id": 3,
    "razrechenie": true,
    "id_plane": 3,
    "id_ekipazha": 3
}
```
