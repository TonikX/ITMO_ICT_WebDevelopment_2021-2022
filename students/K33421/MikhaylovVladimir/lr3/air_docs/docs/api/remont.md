# Ремонт

Информация об эндпоинтах, связанных с ремонтом самолёта

## Cписок всех записей в ремонтном журнале

**URL** : `/api/remont/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "polomka": "Вход из строя двигателя №2",
        "id_plane": 1
    }
]
```
## Добавить самолёт в ремонт с указанием причины

**URL** : `/api/remont/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 2,
    "polomka": "Поломка шасси",
    "id_plane": 2
}
```

## Просмотр, изменение и удаление самолёта в ремонте

**URL** : `api/remont/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 2,
    "polomka": "Поломка шасси",
    "id_plane": 2
}
```

## Детальный просмотр самолётов, характеристик и поломки

**URL** : `api/remont/depth/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "Remont": [
        {
            "id": 1,
            "polomka": "Вход из строя двигателя №2",
            "id_plane": {
                "id": 1,
                "type": "Boing",
                "number": "10-20",
                "mesta": 600,
                "speed": 850,
                "avia": "Россфлот"
            }
        },
        {
            "id": 2,
            "polomka": "Поломка шасси",
            "id_plane": {
                "id": 2,
                "type": "Boing",
                "number": "20-20",
                "mesta": 200,
                "speed": 900,
                "avia": "Россфлот"
            }
        }
    ]
}
```