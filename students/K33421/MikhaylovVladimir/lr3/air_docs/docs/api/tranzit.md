# Транзит

Информация об эндпоинтах, связанных с пересадкой на рейсах

## Cписок всех записей в "транзите"

**URL** : `/api/tranzit/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "punkt_peresadki": "Владивосток"
    }
]
```
## Добавить новый пересадочный пункт

**URL** : `/api/tranzit/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 2,
    "punkt_peresadki": "Пхиньянь"
}
```

## Просмотр, изменение и удаление пересадки

**URL** : `api/tranzit/<int:pk>/`

**Method** : `POST`, `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 2,
    "punkt_peresadki": "Пхиньянь"
}
```
