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
        "polomka": "Шасси",
        "id_plane": 4
    },
    {
        "id": 2,
        "polomka": "Хвостовое оперение",
        "id_plane": 2
    },
    {
        "id": 3,
        "polomka": "Турбина",
        "id_plane": 6
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
    "id": 6,
    "polomka": "Задняя дверь",
    "id_plane": 7
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
    "id": 6,
    "polomka": "Задняя и передние двери",
    "id_plane": 7
}
```

## Детальный просмотр "подноготной" самолёта

**URL** : `api/remont/depth/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
            "id": 6,
            "polomka": "Задняя и передние двери",
            "id_plane": {
                "id": 7,
                "type": "Боинг",
                "number": "787-8",
                "mesta": 347,
                "speed": 918,
                "avia": "QATAR AIRWAYS"
            }
    }
]
```