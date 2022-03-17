Выводит информацию об определенной 
альпинисте и позвольяет менять данные о нем

**URL** : `/climbers/<int:pk>`

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
}
```