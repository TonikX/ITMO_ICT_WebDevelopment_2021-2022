# Рабочие

Информация об эндпоинтах, связанных с работниками компании

## Cписок всех рабочих

**URL** : `/api/workers/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "fio": "Косарев Сергей Владимирович",
        "age": 32,
        "education": "VSH",
        "stajh_raboty": 2,
        "passport": "1234567890"
    },
    {
        "fio": "Воздушный Антон Игоревич",
        "age": 39,
        "education": "VSH",
        "stajh_raboty": 5,
        "passport": "0000213432"
    },
    {
        "fio": "Орлов Иван Юрьевич",
        "age": 48,
        "education": "VSH",
        "stajh_raboty": 12,
        "passport": "1209347652"
    },
    {
        "fio": "Mikh Vlad Vlad",
        "age": 18,
        "education": "",
        "stajh_raboty": 0,
        "passport": ""
    }
]
```
## Добавить нового рабочего

**URL** : `/api/worker/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "username": "Прочный",
    "fio": "Прочный Валерий Юрьевич",
    "age": 27,
    "education": "VSH",
    "stajh_raboty": 2,
    "passport": "1029345133"
}
```

## Просмотр, изменение и удаление рабочего

**URL** : `api/worker/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "fio": "Прочный Валерий Юрьевич",
    "age": 27,
    "education": "VSH",
    "stajh_raboty": 2,
    "passport": "1029345133"
}
```
