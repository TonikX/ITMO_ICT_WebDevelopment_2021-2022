Выводит информацию обо всех вершинах

**URL** : `/peaks`

**HTTP 200 OK**

**Allow:** `GET, HEAD, OPTIONS`

**Content-Type:** `application/json`

**Vary:** `Accept`


```json
{
        "id": 1,
        "name": "Great Peak",
        "country": "Russia",
        "height": "6000",
        "climbing_duration": "2",
        "route_description": "A very difficult route"
    },
    {
        "id": 2,
        "name": "Mountain peak",
        "country": "China",
        "height": "6000",
        "climbing_duration": "3",
        "route_description": "Very difficult"
    },
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