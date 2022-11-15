# Рейс

Информация об эндпоинтах, связанных с рейсами

## Cписок всех рейсов

**URL** : `/api/reys/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "number": 10,
        "distance": 1345,
        "punkt_start": "Дрезден",
        "punkt_end": "Амстердам",
        "id_tranzita": null
    },
    {
        "number": 567,
        "distance": 5678,
        "punkt_start": "Майами",
        "punkt_end": "Иртыш",
        "id_tranzita": 2
    },
    {
        "number": 1234,
        "distance": 1234,
        "punkt_start": "Москва",
        "punkt_end": "Казань",
        "id_tranzita": null
    }
]
```
## Добавить новый рейс

**URL** : `/api/reys/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "number": 543,
    "distance": 718,
    "punkt_start": "Москва (Внуково)",
    "punkt_end": "Санкт-Петербург",
    "id_tranzita": null
}
```

## Просмотр, изменение и удаление рейса

**URL** : `api/reys/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "number": 543,
    "distance": 723,
    "punkt_start": "Москва (Шереметьево)",
    "punkt_end": "Санкт-Петербург",
    "id_tranzita": null
}
```

