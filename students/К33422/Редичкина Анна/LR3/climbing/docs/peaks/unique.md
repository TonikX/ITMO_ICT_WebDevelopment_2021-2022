Предоставить информацию о том, сколько альпинистов побывало на каждой
горе.

**URL** : `peaks/<int:pk>/unique_climbers`

**HTTP 200 OK**

**Allow:** `GET, PUT, PATCH, HEAD, OPTIONS`

**Content-Type:** `application/json`

**Vary:** `Accept`

```json
 {
        "id": 1,
        "first_name": "Максим",
        "last_name": "Иванов",
        "address": "улица Савушкина, 4",
        "club": 1
    },
    {
        "id": 2,
        "first_name": "Анна",
        "last_name": "Редичкина",
        "address": "ул Татищева, 16",
        "club": 1
    }
```