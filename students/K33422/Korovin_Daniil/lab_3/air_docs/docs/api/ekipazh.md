# Экипаж

Информация об эндпоинтах, связанных с экипажем судна.

## Cписок всех экипажей

**URL** : `/api/ekipazh/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "name": "Красный"
    },
    {
        "id": 2,
        "name": "Синий"
    },
    {
        "id": 3,
        "name": "Блестящий"
    },
    {
        "id": 6,
        "name": "Белый"
    }
]
```
## Добавить экипаж

**URL** : `/api/ekipazh/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "name": "Новый"
}
```

## Просмотр, изменение и удаление экипажа

**URL** : `api/ekipazh/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 7,
    "name": "Новый (почти)"
}
```
