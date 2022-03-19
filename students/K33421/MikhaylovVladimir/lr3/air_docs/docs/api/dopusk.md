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
            "number": 1,
            "distance": 3000,
            "punkt_start": "Санкт-Петербург",
            "punkt_end": "Япония",
            "id_tranzita": 1
        },
        "id_ekipazha": {
            "id": 1,
            "name": "Ввысь"
        },
        "nalichie_dopuska": true
    },
    {
        "id": 2,
        "number_reysa": {
            "number": 1,
            "distance": 3000,
            "punkt_start": "Санкт-Петербург",
            "punkt_end": "Япония",
            "id_tranzita": 1
        },
        "id_ekipazha": {
            "id": 2,
            "name": "Старт"
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
    "number_reysa": 1,
    "id_ekipazha": 2,
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
    "id": 3,
    "nalichie_dopuska": true,
    "number_reysa": 1,
    "id_ekipazha": 2
}
```
