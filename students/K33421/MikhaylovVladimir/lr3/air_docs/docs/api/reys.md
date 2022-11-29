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
        "number": 1,
        "distance": 3000,
        "punkt_start": "Санкт-Петербург",
        "punkt_end": "Япония",
        "id_tranzita": 1
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
    "number": 2,
    "distance": 4000,
    "punkt_start": "Москва",
    "punkt_end": "Париж",
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
    "number": 2,
    "distance": 4000,
    "punkt_start": "Москва",
    "punkt_end": "Париж",
    "id_tranzita": null
}
```
