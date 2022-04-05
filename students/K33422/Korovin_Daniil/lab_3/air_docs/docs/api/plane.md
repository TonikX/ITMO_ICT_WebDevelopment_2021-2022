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
        "type": "Боинг",
        "number": "737-500",
        "mesta": 167,
        "speed": 900,
        "avia": "Аэрофлот"
    },
    {
        "id": 2,
        "type": "Боинг",
        "number": "747-8",
        "mesta": 450,
        "speed": 950,
        "avia": "Россия"
    },
    {
        "id": 3,
        "type": "Airbus",
        "number": "A350",
        "mesta": 550,
        "speed": 935,
        "avia": "Аэрофлот"
    },
    {
        "id": 6,
        "type": "Airbus",
        "number": "A330",
        "mesta": 320,
        "speed": 850,
        "avia": "Аэрофлот"
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
    "type": "Боинг",
    "number": "787-8",
    "mesta": 350,
    "speed": 918,
    "avia": "QATAR AIRWAYS"
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
    "id": 7,
    "type": "Боинг",
    "number": "787-8",
    "mesta": 347,
    "speed": 918,
    "avia": "QATAR AIRWAYS"
}
```