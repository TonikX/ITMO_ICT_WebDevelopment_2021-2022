# Самолёт

Информация об эндпоинтах, связанных с самолётами аэропорта

## Cписок всех самолётов

**URL** : `/api/planes/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "type": "Boing",
        "number": "10-20",
        "mesta": 600,
        "speed": 850,
        "avia": "Россфлот"
    },
    {
        "id": 2,
        "type": "Boing",
        "number": "20-20",
        "mesta": 200,
        "speed": 900,
        "avia": "Россфлот"
    },
    {
        "id": 3,
        "type": "Jet",
        "number": "123-31",
        "mesta": 40,
        "speed": 1050,
        "avia": "Россфлот"
    }
]
```
## Добавить новый самолёт

**URL** : `/api/plane/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "type": "Boing",
    "number": "20-40",
    "mesta": 300,
    "speed": 950,
    "avia": "Россфлот"
}
```

## Просмотр, изменение и удаление самолёта

**URL** : `api/plane/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 4,
    "type": "Boing",
    "number": "20-40",
    "mesta": 300,
    "speed": 950,
    "avia": "Россфлот"
}
```