# Допуск

Информация об допуске экипажа на конкретный рейс

## Cписок всех допусков

**URL** : `/api/dopusk/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "number_reysa": {
            "number": 45,
            "distance": 48,
            "punkt_start": "Москва (Внуково)",
            "punkt_end": "Москва (Шереметьево)",
            "id_tranzita": null
        },
        "id_ekipazha": {
            "id": 1,
            "name": "Красный"
        },
        "nalichie_dopuska": true
    },
    {
        "id": 5,
        "number_reysa": {
            "number": 1234,
            "distance": 1234,
            "punkt_start": "Москва",
            "punkt_end": "Казань",
            "id_tranzita": null
        },
        "id_ekipazha": {
            "id": 6,
            "name": "Белый"
        },
        "nalichie_dopuska": true
    }
]
```
## Добавить новый допуск

**URL** : `/api/dopusk/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "number_reysa": 354,
    "id_ekipazha": 7,
    "nalichie_dopuska": true
}
```

## Просмотр, изменение и удаление допуска

**URL** : `api/dopusk/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 6,
    "nalichie_dopuska": false,
    "number_reysa": 354,
    "id_ekipazha": 7
}
```

