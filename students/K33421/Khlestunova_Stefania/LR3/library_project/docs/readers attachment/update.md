# Update ReadersAttachment

Просмотр/изменение/удаление данных об опр. записе о регистрации читателя в зале.

**URL** : `/library/readers_attachment/<int:pk>/update/`

**Allow** : `GET, PUT, PATCH, HEAD, OPTIONS`

**HTTP 200 OK**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
{
    "id": 2,
    "attach_date": "2022-01-17T16:24:23Z",
    "reader": 2,
    "hall": 2
}
```