Выводит информацию об определенной вершине 
и позвольяет менять данные о ней

**URL** : `peaks/<int:pk>`

**HTTP 200 OK**

**Allow:** `GET, PUT, PATCH, HEAD, OPTIONS`

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
}
```