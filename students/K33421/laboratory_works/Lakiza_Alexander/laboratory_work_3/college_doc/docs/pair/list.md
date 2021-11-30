### Просмотреть данные о паре 

**URL** : `/pair/list/`

**HTTP 200 OK**

**Allow** : GET, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
[
    {
        "id": 1,
        "pair_number": 1,
        "name_day": "Mon",
        "room": 31,
        "group": 1,
        "teacher": 1,
        "subject": 1
    },
    {
        "id": 2,
        "pair_number": 1,
        "name_day": "Mon",
        "room": 27,
        "group": 2,
        "teacher": 2,
        "subject": 2
    }
]
```