### Просмотреть данные о студентах 

**URL** : `/student/list/`

**HTTP 200 OK**

**Allow** : GET, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
[
    {
        "id": 1,
        "group": [
            {
                "id": 1,
                "name": "A100"
            }
        ],
        "first_name": "Кирилл",
        "last_name": "Чернышев"
    },
    {
        "id": 2,
        "group": [
            {
                "id": 2,
                "name": "B201"
            }
        ],
        "first_name": "Никита",
        "last_name": "Паращенко"
    }
]
```