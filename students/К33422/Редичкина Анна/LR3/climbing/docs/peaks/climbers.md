Количество восхождений каждого альпиниста на каждую вершину

**URL** : `peaks/<int:pk>/climbers`

**HTTP 200 OK**

**Allow:** `GET, HEAD, OPTIONS`

**Content-Type:** `application/json`

**Vary:** `Accept`

```json
  {
        "first_name": "Максим",
        "last_name": "Иванов",
        "address": "улица Савушкина, 4",
        "club": 1,
        "climbings_on_peak": 1
    },
    {
        "first_name": "Анна",
        "last_name": "Редичкина",
        "address": "ул Татищева, 16",
        "club": 1,
        "climbings_on_peak": 1
    }
```