# Полёт

Информация об эндпоинтах, связанных с полётом самолёта по рейсу

## Cписок всех полётов в журнале

**URL** : `/api/polet/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id_poleta": 1,
        "date_start": "2021-01-22",
        "time_start": "18:06:46",
        "date_end": "2021-01-22",
        "time_end": "19:06:46",
        "sell_tickets": 29,
        "made_reys": 16,
        "date_start_tranzit": null,
        "time_start_tranzit": null,
        "date_end_tranzit": null,
        "time_end_tranzit": null,
        "number_reysa": 354,
        "id_plane": 1
    },
    {
        "id_poleta": 2,
        "date_start": "2021-01-22",
        "time_start": "21:18:24",
        "date_end": "2021-01-23",
        "time_end": "19:06:46",
        "sell_tickets": 456,
        "made_reys": 345,
        "date_start_tranzit": "2021-01-23",
        "time_start_tranzit": "12:04:05",
        "date_end_tranzit": "2021-01-23",
        "time_end_tranzit": "17:35:44",
        "number_reysa": 567,
        "id_plane": 2
    }
]
```
## Добавить полёт

**URL** : `/api/polet/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id_poleta": 5,
    "date_start": "2021-01-26",
    "time_start": "18:30:00",
    "date_end": "2021-01-26",
    "time_end": "20:30:00",
    "sell_tickets": 145,
    "made_reys": 267,
    "date_start_tranzit": null,
    "time_start_tranzit": null,
    "date_end_tranzit": null,
    "time_end_tranzit": null,
    "number_reysa": 1234,
    "id_plane": 3
}
```

## Просмотр, изменение и удаление полёта из журнала

**URL** : `api/polet/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id_poleta": 5,
    "date_start": "2021-01-26",
    "time_start": "18:30:00",
    "date_end": "2021-01-26",
    "time_end": "20:35:00",
    "sell_tickets": 147,
    "made_reys": 267,
    "date_start_tranzit": null,
    "time_start_tranzit": null,
    "date_end_tranzit": null,
    "time_end_tranzit": null,
    "number_reysa": 1234,
    "id_plane": 3
}
```

## Детальный просмотр полёта с типом рейса и видом самолёта

**URL** : `api/polet/detail/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id_poleta": 5,
        "id_plane": {
            "id": 3,
            "type": "Airbus",
            "number": "A350",
            "mesta": 550,
            "speed": 935,
            "avia": "Аэрофлот"
        },
        "number_reysa": {
            "number": 1234,
            "distance": 1234,
            "punkt_start": "Москва",
            "punkt_end": "Казань",
            "id_tranzita": null
        },
        "date_start": "2021-01-26",
        "time_start": "18:30:00",
        "date_end": "2021-01-26",
        "time_end": "20:35:00",
        "sell_tickets": 147,
        "made_reys": 267,
        "date_start_tranzit": null,
        "time_start_tranzit": null,
        "date_end_tranzit": null,
        "time_end_tranzit": null
    }
]
```