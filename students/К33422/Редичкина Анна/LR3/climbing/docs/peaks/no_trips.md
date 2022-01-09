Выводит список вершин, на которых не было восхождений

**URL** : `/peaks/not_trip`

**HTTP 200 OK**

**Allow:** `GET, HEAD, OPTIONS`

**Content-Type:** `application/json`

**Vary:** `Accept`

```json
{
        "id": 3,
        "name": "Another peak",
        "country": "China",
        "height": "2000",
        "climbing_duration": "1",
        "route_description": "Easy"
    },
    {
        "id": 4,
        "name": "The Highest Peak",
        "country": "China",
        "height": "8000",
        "climbing_duration": "5",
        "route_description": "Very hard"
    }
```