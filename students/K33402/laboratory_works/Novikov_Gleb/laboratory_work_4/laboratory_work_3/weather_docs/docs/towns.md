# Город

## Список городов

Получение списка всех городов.

**URL** : `/town/all/`

**Method** : `GET`

**Auth required** : YES

**Request body** : empty

**Success Response**

**Code** : `200 OK`

```json
{
    "towns": [
        {
            "id": 1,
            "name": "Sochi",
            "lon": 48.232092,
            "lat": 32.489039
        },
        {
            "id": 2,
            "name": "Moscow",
            "lon": 37.592002,
            "lat": 55.743209
        }
    ]
}
```

### Failure

**Code** : `401 Unauthorized`

## Добавление города

Добавление нового города с указание долготы, широты и кода страны.

**URL** : `/town/create`

**Method** : `POST`

**Auth required** : YES

**Request body** : 
```json
{
    "name": "Moscow",
    "lon": 37.592002,
    "lat": 55.743209
}
```

**Success Response**

**Code** : `200 OK`

```json
{
    "id": 2,
    "name": "Moscow",
    "lon": 37.592002,
    "lat": 55.743209
}
```
