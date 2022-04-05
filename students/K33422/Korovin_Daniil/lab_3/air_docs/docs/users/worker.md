# Работник

Информация об эндпоинтах, связанных с работниками компании

## Cписок всех работников

**URL** : `/api/workers/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
        {
            "fio": "Янов Филипп Андреевич",
            "age": 20,
            "education": "VSN",
            "stajh_raboty": 1,
            "passport": "3424342453"
        },
        {
            "fio": "Волков Вениамин Сергеевич",
            "age": 37,
            "education": "VSH",
            "stajh_raboty": 14,
            "passport": "5678999012"
        },
        {
            "fio": "Лодырев Александр Сергеевич",
            "age": 54,
            "education": "VSH",
            "stajh_raboty": 26,
            "passport": "2456111334"
        },
        {
            "fio": "Михайлов Станислав Вальерьянович",
            "age": 45,
            "education": "VSH",
            "stajh_raboty": 24,
            "passport": "3423456897"
        }
]
```
## Добавить нового работника

**URL** : `/api/worker/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "username": "Kaltymbek",
    "fio": "Дьяков Калтымбек Никарагуавич",
    "age": 20,
    "education": "VSN",
    "stajh_raboty": 2,
    "passport": "1123444555"
}
```

## Просмотр, изменение и удаление работника

**URL** : `api/worker/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "fio": "Дьяков Калтымбек Никарагуавич",
    "age": 21,
    "education": "VSH",
    "stajh_raboty": 3,
    "passport": "1123444555"
}
```

