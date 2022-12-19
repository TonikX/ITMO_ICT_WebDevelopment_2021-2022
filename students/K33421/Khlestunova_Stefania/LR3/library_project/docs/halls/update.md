# Update Hall

Просмотр/изменение/удаление информации об опр. зале.

**URL** : `/library/halls/<int:pk>/update/`

**Allow** : `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`

**HTTP 200 OK**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
{
    "id": 1,
    "hall_num": 2,
    "hall_name": "МегаКнига",
    "capacity": 200
}
```