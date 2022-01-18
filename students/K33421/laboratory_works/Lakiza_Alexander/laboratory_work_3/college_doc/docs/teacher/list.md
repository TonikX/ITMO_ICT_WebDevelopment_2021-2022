### Просмотреть данные о преподавателях 

**URL** : `/teacher/list/`

**HTTP 200 OK**

**Allow** : GET, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
[
    {
        "id": 1,
        "subjects": [
            {
                "id": 1,
                "name": "Математика"
            }
        ],
        "first_name": "Светлана",
        "last_name": "Козлова",
        "room": "31"
    },
    {
        "id": 2,
        "subjects": [
            {
                "id": 2,
                "name": "Русский язык"
            }
        ],
        "first_name": "Валентина",
        "last_name": "Шерстнева",
        "room": "26"
    }
]
```